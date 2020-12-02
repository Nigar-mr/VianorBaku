from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from django.utils import timezone
from django.views import generic
from django.views.generic.base import ContextMixin

from .models import Unique, FirstMenu, \
    SecondMenu, FooterMenu, FooterSubMenu, Newsletter, \
    Social, SocialText, SlideImage, Client, FeaturedBlocks, \
    Discount, DiscountProducts

from tyres.models import CarMarka, CarModel, CarMotor, \
    CarYear, Tyres, Brand
from orders.models import Card_list, OrderProducts
from .forms import LetterEForm
from orders.forms import OrderForm


# Create your views here.


class CommonMixin(ContextMixin):

    def get_context_data(self, **kwargs):
        context = super(CommonMixin, self).get_context_data(**kwargs)
        context['unique'] = Unique.objects.last()
        context['block'] = FeaturedBlocks.objects.all()
        context['first_menu'] = FirstMenu.objects.all()
        context['second_menu'] = SecondMenu.objects.all()
        context['footer_menu'] = FooterMenu.objects.all()
        context['footer_sub_menu'] = FooterSubMenu.objects.all()
        context['newsletter'] = Newsletter.objects.last()
        context['social_text'] = SocialText.objects.last()
        context['social'] = Social.objects.all()
        context['slide'] = SlideImage.objects.all()
        context['brands'] = Brand.objects.all()
        context['products'] = Tyres.objects.all()
        context['last_products'] = Tyres.objects.all().order_by('-id')[:5]

        context['tyres_width'] = Tyres.objects.values_list('width', flat=True).distinct()
        context['tyres_height'] = Tyres.objects.values_list('height', flat=True).distinct()
        context['tyres_radius'] = Tyres.objects.values_list('radius', flat=True).distinct()

        user = self.request.session.session_key
        cards = Card_list.objects.filter(user__session_key=user)
        context['order'] = cards
        my_list = []
        for items in cards:
            total = items.total_price
            my_list.append(total)
        context['total'] = sum(my_list)
        context['count'] = len(my_list)

        return context


class Filtered(CommonMixin, generic.ListView):
    template_name = 'shop-list.html'
    context_object_name = 'filter'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(Filtered, self).get_context_data(**kwargs)
        context['checked_brand'] = self.request.GET.getlist('brand[]')
        context['checked_width'] = self.request.GET.getlist('width[]')
        context['checked_height'] = self.request.GET.getlist('height[]')
        context['checked_radius'] = self.request.GET.getlist('radius[]')

        return context

    def post(self, request):
        if self.request.is_ajax():
            if self.request.POST.get('namee') == 'remove':
                data_id = self.request.POST.get('item_id')
                tyres = Tyres.objects.filter(id=data_id).last()
                card_list = Card_list.objects.filter(product_id=data_id).last()
                if tyres:
                    tyres.add_to_card = False
                    card_list.quantity = 0
                    tyres.save()
                    card_list.delete()
            elif self.request.POST.get('namee') == 'add_to_cart':
                session = self.request.session.session_key
                data_id = self.request.POST.get('data_id')
                tyres = Tyres.objects.filter(id=data_id).first()
                card_list = Card_list.objects.filter(product_id=data_id).first()
                client = Client.objects.filter(session_key=session).first()

                if not client:
                    Client.objects.create(
                        session_key=session
                    )

                client = Client.objects.filter(session_key=session).first()
                card = Card_list.objects.filter(product_id=data_id, user=client).first()
                if not card:
                    Card_list.objects.create(
                        product_id=data_id,
                        quantity=1,
                        user_id=client.id,
                        total_price=tyres.price,
                    )
                    tyres.add_to_card = True
                    tyres.save()
                else:
                    card_list.quantity += 1
                    card_list.total_price = tyres.price * card_list.quantity
                    card_list.save()

    def get_queryset(self):
        query = Tyres.objects.all()
        model = self.request.GET.get('model')
        marka = self.request.GET.get('marka')
        motor = self.request.GET.get('motor')
        elements = self.request.GET

        if 'marka' and 'model' and 'motor' and 'year' in self.request.GET:
            query = query.filter(
                Q(car__marka__marka=marka) &
                Q(car__model__model=model) &
                Q(car__motor__motor=motor)
            )

        if 'brand[]' in elements:
            query = query.filter(brand__brand__in=elements.getlist('brand[]'))

        if 'width[]' in elements:
            query = query.filter(width__in=elements.getlist('width[]'))

        if 'height[]' in elements:
            query = query.filter(height__in=elements.getlist('height[]'))

        if 'radius[]' in elements:
            query = query.filter(radius__in=elements.getlist('radius[]'))

        if "ASC" in elements:
            return query.order_by('price')
        else:
            return query.order_by('-price')

        return query


class HomeView(CommonMixin, generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['marka'] = CarMarka.objects.all()
        context['model'] = CarModel.objects.all()
        context['motor'] = CarMotor.objects.all()
        context['year'] = CarYear.objects.all()
        context['brands'] = Brand.objects.all()
        context['letter_form'] = LetterEForm()
        context['new_arrivals'] = Tyres.objects.all().order_by('-id')[:8]
        discount = Discount.objects.all()
        expiry_date = discount.values_list('expiry_date', flat=True)
        current_date = timezone.now()
        for date in expiry_date:
            context['discount'] = discount.filter(expiry_date__range=[current_date, date])
            filters = discount.filter(expiry_date__range=[current_date, date]).values('discount_name')
            # print(filters)
            # for i in filters:
            #     print(i)
            discount_products = Tyres.objects.filter(product__diccount__discount_name='Qelebe')
            print(discount_products)
            # print(Tyres.objects.filter(product__diccount__discount_name='Qelebe'))

            context['discount_products'] = discount_products
        return context

    def post(self, request):
        if self.request.POST.get('namee') == 'remove':
            print('REMOVEE')
            data_id = self.request.POST.get('item_id')
            tyres = Tyres.objects.filter(id=data_id).last()
            card_list = Card_list.objects.filter(product_id=data_id).last()
            if tyres:
                tyres.add_to_card = False
                card_list.quantity = 0
                tyres.save()
                card_list.delete()

        if 'email' in self.request.POST:
            form = LetterEForm(self.request.POST)
            if form.is_valid():
                form.save()

        else:
            marka_id = self.request.POST.get('marka_id')
            model_id = self.request.POST.get('model_id')
            motor_id = self.request.POST.get('motor_id')
            model = CarModel.objects.filter(marka_id=marka_id)
            motor = CarMotor.objects.filter(model_id=model_id)
            year = CarYear.objects.filter(motor_id=motor_id)
            result = []

            for i in model:
                result.append({
                    'model': i.model,
                    'id': i.id
                })

            for i in motor:
                result.append({
                    'motor': i.motor,
                    'id': i.id
                })
            for i in year:
                result.append({
                    "year": i.year,
                    'id': i.id
                })

            return JsonResponse({
                'data': result
            })


class CheckoutView(CommonMixin, generic.CreateView):
    template_name = 'checkout.html'
    model = OrderProducts
    success_url = "/"
    form_class = OrderForm

    def form_valid(self, form):
        user = self.request.session.session_key
        cards = Card_list.objects.filter(user__session_key=user)
        form.save()
        for card_item in cards:
            OrderProducts.objects.create(
                product_name=card_item.product.name,
                quantity=card_item.quantity,
                total_price=card_item.total_price,
                order=form.instance
            )
            cards.delete()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CheckoutView, self).get_context_data(**kwargs)
        context['order_form'] = OrderForm()
        user = self.request.session.session_key
        cards = Card_list.objects.filter(user__session_key=user)
        context['order'] = cards
        my_list = []
        for items in cards:
            total = items.total_price
            my_list.append(total)
        context['total'] = sum(my_list)
        return context


class CartView(CommonMixin, generic.ListView):
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        user = self.request.session.session_key
        card_products = Card_list.objects.filter(user__session_key=user)
        context['card_list'] = card_products
        return context

    def get_queryset(self):
        pass

    def post(self, request):
        if self.request.is_ajax():
            if request.POST.get('namee') == 'quantity':
                data_id = request.POST.get('data_id')
                quantity = request.POST.get('quantity')
                price = request.POST.get('price')
                total = int(price) * int(quantity)
                products = Card_list.objects.filter(product_id=data_id).last()
                if products:
                    products.total_price = total
                    products.quantity = quantity
                    products.save()
            elif request.POST.get('namee') == 'remove':
                data_id = request.POST.get('item_id')
                tyres = Tyres.objects.filter(id=data_id).last()
                card_list = Card_list.objects.filter(product_id=data_id).last()
                if tyres:
                    tyres.add_to_card = False
                    card_list.quantity = 0
                    tyres.save()
                    card_list.delete()
