from django.urls import path,include,re_path
import xadmin
from django.views.static import serve
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

from MxShop.settings import MEDIA_ROOT
# from goods.view_base import GoodsListView

from rest_framework.documentation import include_docs_urls
from goods.views import GoodsListViewSet, BannerViewset, IndexCategoryViewset
from rest_framework.routers import DefaultRouter

from user_operation.views import UserFavViewset, LeavingMessageViewset, AddressViewset
from users.views import SmsCodeViewset, UserViewset
from trade.views import ShoppingCartViewset, OrderViewset, AlipayView

router = DefaultRouter()
from goods.views import CategoryViewSet
###配置goods的url
router.register(r'goods', GoodsListViewSet,basename='goods')
#### 配置Category的url
router.register(r'categorys', CategoryViewSet,basename='categorys')
# ####配置codes的url
router.register(r'code', SmsCodeViewset,basename="code")
####配置注册url
router.register(r'users', UserViewset, basename="users")
#### 配置用户收藏的url
router.register(r'userfavs', UserFavViewset, basename="userfavs")
####配置用户留言的url
router.register(r'messages', LeavingMessageViewset, basename="messages")
####配置收货地址
router.register(r'address',AddressViewset , basename="address")
####配置购物车的url
router.register(r'shopcarts',ShoppingCartViewset,basename='shopcarts')
####配置订单的url
router.register(r'orders', OrderViewset, basename="orders")
####配置首页轮播图的url
router.register(r'banners', BannerViewset, basename="banners")
####首页系列商品展示url
router.register(r'indexgoods', IndexCategoryViewset, basename="indexgoods")
from django.views.generic import TemplateView
urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    path('ueditor/',include('DjangoUeditor.urls' )),
    #文件
    path('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),
    #drf文档，title自定义
    path('docs/',include_docs_urls(title='MxShop_1906c')),
    #商品列表页
    re_path('^', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('login/',obtain_jwt_token),
    # 配置支付宝支付相关接口的url
    path('alipay/return/', AlipayView.as_view()),
    # 首页
    path('index/', TemplateView.as_view(template_name='index.html'), name='index'),
    ##第三方登录
    path('',include('social_django.urls',namespace='scoial')),


]