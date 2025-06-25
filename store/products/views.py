
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView


from common.views import TitleMixin
from products.models import ProductsCategory, Products


class IndexView(TitleMixin, TemplateView):
    template_name = 'products/index.html'
    title = 'Parametric'


class ProductsListView(TitleMixin, ListView):
    model = Products
    template_name = 'products/products.html'
    paginate_by = 3
    title = 'Parametric - Каталог'

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        context['categories'] = ProductsCategory.objects.all()
        return context

    @login_required
    def basket_add(request, product_id):
        Basket.create_or_update(product_id, request.user)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

    @login_required
    def basket_remove(request, basket_id):
        basket = Basket.objects.get(id=basket_id)
        basket.delete()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

# class ProductView(View):
#     def get(self, request):
#         # products = Products.objects.all()
#         context = {
#                 'product_categories': ProductsCategory.objects.all(),
#                 'title': 'Parametric',
#                 # 'title': 'Parametric - Каталог',
#                 'products': Products.objects.all(),
#             }
#         return render(request, 'index.html',"products/base.html", context)


# def index(request):
#     context = {
#         'product_categories': ProductsCategory.objects.all(),
#         'title': 'Parametric',
#     }
#
#     return render(request, 'index.html', context)
#
#
# def products(request):
#     context = {
#         'title': 'Parametric - Каталог',
#         'products': Products.objects.all(),
#         'product_categories': ProductsCategory.objects.all(),
#     }
#
#     return render(request, 'products/products.html', context)
