from datetime import date
from django.test import TestCase, RequestFactory, Client, TransactionTestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser, User
from django.contrib.auth import authenticate
import json
from parameterized import parameterized, parameterized_class
from .views import (index, SignUp,
                    CafeListView, DishListView,
                    myOrders, CartListView,
                    create_order, deleteOrder,
                    user_account_change, complaints,
                    complaintsCreated, complaintsCompleted,
                    ManagerOrders, managerComplains,
                    managerComplainsResolve, ManagerOrdersConfirmed,
                    ManagerOrdersDeclined, switch_order,
                    ManagerCafe, ManagerDish,
                    ManagerDishUpdate, showhide_dish, delete_dish)
from .models import (Cafe, Menu, Dish, Order, OrderDetail, Complaint)


class TestManagerVews(TestCase):
    def setUp(self):
        self.manager = get_user_model().objects.create_superuser(
            username='test',
            password='12test12',
            email='test@example.com'
        )
        self.user = get_user_model().objects.create_superuser(
            username='user',
            password='12test12',
            email='user@example.com'
        )
        self.manager.save()
        self.user.save()
        self.timestamp = date.today()
        self.client.login(username='test', password='12test12')
        self.cafe1 = Cafe(name='cafe1', location='inno', manager=self.manager)
        self.cafe1.save()
        self.menu1 = Menu(cafe=self.cafe1)
        self.menu1.save()
        self.dish1 = Dish(name='dish1',
                          price=123,
                          visible=True,
                          in_menu=True, cafe=self.cafe1)
        self.dish1.save()
        self.order1 = Order(
            destination='inno',
            cafe=self.cafe1,
            customer=self.user,
            confirmed=True
        )
        self.order1.save()
        self.order_detail1 = OrderDetail(
            dishes=self.dish1,
            quantity=2,
            order=self.order1
        )
        self.order_detail1.save()

        self.complaint1 = Complaint(
            description='this is description',
            complaint_title='not good',
            complaint_order_number='1',
            complaint_contact='contact',
        )
        self.complaint1.save()

    def tearDown(self):
        self.manager.delete()
        self.cafe1.delete()
        self.menu1.delete()

    def test_manager_orders(self):
        response = self.client.get(reverse('manager_orders'))
        self.assertTrue(response.status_code, 200)

    def test_manager_managerComplains(self):
        response = self.client.get(reverse('managerComplains'))
        self.assertEqual(response.status_code, 200)

    def test_manager_managerComplainsResolve(self):
        response = self.client.get(
            reverse('managerComplainsResolve', kwargs={
                'id': self.complaint1.id
            }))
        self.assertEqual(response.status_code, 200)

    def test_manager_manager_confirmed(self):
        response = self.client.get(reverse('manager_confirmed'))
        self.assertEqual(response.status_code, 200)

    def test_manager_manager_declined(self):
        response = self.client.get(reverse('manager_declined'))
        self.assertEqual(response.status_code, 200)

    def test_manager_switch_order(self):
        response = self.client.get(reverse('switch_order', kwargs={
            'id': self.order1.id, 'status': 0}))
        self.assertEqual(response.status_code, 200)

    def test_manager_manager_cafe(self):
        response = self.client.get(reverse('manager_cafe'))
        self.assertEqual(response.status_code, 200)

    def test_manager_manager_dish(self):
        response = self.client.get(reverse('manager_dish'))
        self.assertEqual(response.status_code, 200)

    def test_manager_manager_dish_update(self):
        response = self.client.get(reverse('manager_dish_update',
                                           kwargs={'pk': self.dish1.pk}),
                                   {
                                       'name': 'dish2',
                                       'price': '33',
                                       'in_menu': True
                                   })
        self.assertEqual(response.status_code, 200)

    def test_manager_showhide_dish(self):
        response = self.client.get(
            reverse('showhide_dish', kwargs={'id': self.dish1.id}))
        self.assertEqual(response.status_code, 200)

    def test_manager_delete_dish(self):
        response = self.client.get(
            reverse('delete_dish', kwargs={'id': self.dish1.pk}))
        self.assertEqual(response.status_code, 200)


# Test User View


class TestUserView(TestCase):
    def setUp(self):
        self.client = Client()
        self.manager1 = get_user_model().objects.create_superuser(
            username='test1',
            password='12test12',
            email='test@example.com'
        )
        self.manager1.save()
        self.user1 = User.objects.create_user(
            'user1', 'user1@user1.com', 'managermanager')
        # self.user.is_staff = True
        # self.client.login(username='user', password='managermanager')
        self.cafe2 = Cafe(name='cafe2', location='inno', manager=self.manager1)
        self.cafe2.save()

        self.order2 = Order(
            destination='inno',
            cafe=self.cafe2,
            customer=self.user1,
            confirmed=True
        )
        self.order2.save()
        self.dish2 = Dish(name='dish2',
                          price=123,
                          visible=True,
                          in_menu=True, cafe=self.cafe2)
        self.dish2.save()

    def test_user_cafes(self):
        response = self.client.get(reverse('cafes'))
        self.assertEqual(response.status_code, 200)

    def test_user_dishes(self):
        response = self.client.get(
            reverse('dishes', kwargs={'id': self.dish2.id}))
        self.assertEqual(response.status_code, 200)

    def test_user_customer_orders(self):
        response = self.client.get(reverse('customer_orders'))
        self.assertEqual(response.status_code, 200)

    def test_user_cart(self):
        response = self.client.get(reverse('cart'))
        self.assertEqual(response.status_code, 200)

    def test_user_new_order(self):
        response = self.client.get(
            reverse('new_order', kwargs={'id': self.order2.id}))
        self.assertEqual(response.status_code, 200)

    def test_user_deleteOrder(self):
        response = self.client.get(
            reverse('deleteOrder', kwargs={'id': self.order2.id}))
        self.assertEqual(response.status_code, 200)

    def test_user_customer_account(self):
        response = self.client.get(reverse('customer_account'))
        self.assertEqual(response.status_code, 200)

    def test_user_customer_complaints(self):
        response = self.client.get(reverse('customer_complaints'))
        self.assertEqual(response.status_code, 200)

    def test_user_customer_complaints_created(self):
        response = self.client.get(reverse('customer_complaints_created'))
        self.assertEqual(response.status_code, 200)

    def test_user_complaintsCompleted(self):
        response = self.client.get(reverse('complaintsCompleted'))
        self.assertEqual(response.status_code, 200)


# def testLogin(self):

#     # cafe_id = Cafe.objects.get(manager=self.user)
#     # qs = Dish.objects.filter(visible=True).filter(cafe=cafe_id)
#     response = self.client.get(
#         reverse('manager_cafe'))
#     self.assertEqual(response.status_code, 200)


class TestVews(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='me', email='jacob@me.com', password='me123451234'
        )
        # self.user.is_staff = True

    def test_user_cart_list_view(self):
        request = self.factory.get(reverse('cart'))
        request.user = self.user
        response = CartListView.as_view()(request)
        self.assertEqual(response.status_code, 200)


# Test Models


class TestModels(TestCase):

    def setUp(self):
        User = get_user_model()
        manager_1 = User.objects.create_user(
            username='manager',
            email='manager@me.com',
            password='manager1234'
        )
        manager_1.is_staff = True

        user_1 = User.objects.create_user(
            username='user',
            email='user@me.com',
            password='password1234'
        )

        self.cafe1 = Cafe.objects.create(
            name='name_1',
            location='location_1',
            manager=manager_1,
            visible=True,
        )
        self.menu1 = Menu.objects.create(
            cafe=self.cafe1,
            visible=True
        )
        self.dish1 = Dish.objects.create(
            name='dish1',
            price=123,
            visible=True,
            in_menu=True,
            cafe=self.cafe1
        )
        self.order1 = Order.objects.create(
            destination='destination',
            cafe=self.cafe1,
            customer=user_1,
            confirmed=True,
            visible=True
        )
        self.order_detail1 = OrderDetail.objects.create(
            dishes=self.dish1,
            quantity=10,
            order=self.order1
        )
        self.complaint1 = Complaint.objects.create(
            description='this is not what I ordered',
            complaint_title='complaint title',
            complaint_order_number=1,
            complaint_contact='some contact',
            complaint_resolved=False,
            visible=True
        )

    def test_complaint_fields(self):
        record = Complaint.objects.get(pk=1)
        self.assertEqual(record, self.complaint1)

    def test_order_detail_fields(self):
        record = OrderDetail.objects.get(pk=1)
        self.assertEqual(record, self.order_detail1)

    def test_order_fields(self):
        record = Order.objects.get(pk=1)
        self.assertEqual(record, self.order1)

    def test_cafe_fields(self):
        record = Cafe.objects.get(pk=1)
        self.assertEqual(record, self.cafe1)

    def test_menu_fields(self):
        record = Menu.objects.get(pk=1)
        self.assertEqual(record, self.menu1)

    def test_dish_fields(self):
        record = Dish.objects.get(pk=1)
        self.assertEqual(record, self.dish1)


# Test View

# class ManagerTestView(TestCase):
#     @classmethod
#     def setUp(cls):
#         number_of_cafes = 10
#         for cafe in range(number_of_cafes):
#             Case.objects.create(

#             )

# TestUrls


class TestUrls(TestCase):

    def test_index_url_resolves(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func.view_class, SignUp)

    def test_cafes_url_resolves(self):
        url = reverse('cafes')
        self.assertEquals(resolve(url).func.view_class, CafeListView)

    def test_dishes_url_resolves(self):
        url = reverse('dishes', args=[1])
        self.assertEquals(resolve(url).func.view_class, DishListView)

    def test_customer_orders_url_resolves(self):
        url = reverse('customer_orders')
        self.assertEquals(resolve(url).func, myOrders)

    def test_cart_url_resolves(self):
        url = reverse('cart')
        self.assertEquals(resolve(url).func.view_class, CartListView)

    def test_new_order_url_resolves(self):
        url = reverse('new_order', args=[1])
        self.assertEquals(resolve(url).func, create_order)

    def test_deleteOrder_url_resolves(self):
        url = reverse('deleteOrder', args=[1])
        self.assertEquals(resolve(url).func, deleteOrder)

    def test_customer_account_url_resolves(self):
        url = reverse('customer_account')
        self.assertEquals(resolve(url).func, user_account_change)

    def test_customer_complaints_url_resolves(self):
        url = reverse('customer_complaints')
        self.assertEquals(resolve(url).func, complaints)

    def test_customer_complaints_created_url_resolves(self):
        url = reverse('customer_complaints_created')
        self.assertEquals(resolve(url).func, complaintsCreated)

    def test_complaintsCompleted_url_resolves(self):
        url = reverse('complaintsCompleted')
        self.assertEquals(resolve(url).func, complaintsCompleted)

    def test_manager_orders_url_resolves(self):
        url = reverse('manager_orders')
        self.assertEquals(resolve(url).func.view_class, ManagerOrders)

    def test_managerComplains_url_resolves(self):
        url = reverse('managerComplains')
        self.assertEquals(resolve(url).func, managerComplains)

    def test_managerComplainsResolve_url_resolves(self):
        url = reverse('managerComplainsResolve', args=[1])
        self.assertEquals(resolve(url).func, managerComplainsResolve)

    def test_manager_confirmed_url_resolves(self):
        url = reverse('manager_confirmed')
        self.assertEquals(resolve(url).func.view_class, ManagerOrdersConfirmed)

    def test_manager_declined_url_resolves(self):
        url = reverse('manager_declined')
        self.assertEquals(resolve(url).func.view_class, ManagerOrdersDeclined)

    # def test_switch_order_url_resolves(self):
    #     url = reverse('switch_order', kwargs={'id': })
    #     self.assertEquals(resolve(url).func, switch_order)

    def test_manager_cafe_url_resolves(self):
        url = reverse('manager_cafe')
        self.assertEquals(resolve(url).func.view_class, ManagerCafe)

    def test_manager_dish_url_resolves(self):
        url = reverse('manager_dish')
        self.assertEquals(resolve(url).func.view_class, ManagerDish)

    def test_manager_dish_update_url_resolves(self):
        url = reverse('manager_dish_update', args=[1])
        self.assertEquals(resolve(url).func.view_class, ManagerDishUpdate)

    def test_showhide_dish_url_resolves(self):
        url = reverse('showhide_dish', args=[1])
        self.assertEquals(resolve(url).func, showhide_dish)

    def test_delete_dish_url_resolves(self):
        url = reverse('delete_dish', args=[1])
        self.assertEquals(resolve(url).func, delete_dish)


# Test user


def custom_name_func(testcase_func, param_num, param):
    return "%s_%s" % (
        testcase_func.__name__,
        parameterized.to_safe_name("_".join(str(x) for x in param.args)),
    )


@parameterized_class(("username", "email", "password"), [
    ("meme", "me@me.com", "password1234"),
])
class CustomUserTests(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            self.username,
            self.email,
            self.password
        )
        self.assertEqual(user.username, self.username)
        self.assertEqual(user.email, self.email)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        admin_user = User.objects.create_superuser(
            self.username,
            self.email,
            self.password
        )
        self.assertEqual(admin_user.username, self.username)
        self.assertEqual(admin_user.email, self.email)
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

    def test_create_manager(self):
        admin_user = User.objects.create_user(
            self.username,
            self.email,
            self.password
        )
        admin_user.is_staff = True
        self.assertEqual(admin_user.username, self.username)
        self.assertEqual(admin_user.email, self.email)
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertFalse(admin_user.is_superuser)


@parameterized_class(("username", "email", "password"), [
    ("will", "me@me.com", "password1234"),
])
class TestAdmin(TestCase):
    User = get_user_model()

    def superuser_test(self):
        superuser = self.User.objects.create_superuser(
            self.username,
            self.email,
            self.password
        )
        self.assertEqual(superuser.username, self.username)
        self.assertEqual(superuser.email, self.email)
        self.assertTrue(superuser.is_active)
        self.assertFalse(superuser.is_staff)
        self.assertFalse(superuser.is_superuser)


@parameterized_class(("username", "email", "password"), [
    ("will", "me@me.com", "password1234"),
])
class TestUser(TestCase):
    User = get_user_model()

    def test_customer(self):
        user = self.User.objects.create_user(
            self.username,
            self.email,
            self.password
        )
        self.assertEqual(user.username, self.username)
        self.assertEqual(user.email, self.email)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

# Test Views
# tc = TestCase('__init__')

# response = c.get('/accounts/login/',
#                  {'username': 'manager', 'password': 'adminadmin'})

# response = c.get(reverse('manager_orders'))
# print(response.status_code)


# def test_manager_manager_orders():
#     response = client.get(reverse('manager_orders'))
#     tc.assertEqual(response.status_code, 200)


# class LoginView(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()
#         self.user = authenticate(username='manager', password='adminadmin')
#         # login = .force_login(user)

#     def test_manager_manager_orders(self):
#         # self.assertTrue((self.user is not None) and self.user.is_authenticated)
#         request = self.factory.get(reverse('manager_orders'))
#         request.user = self.user
#         response = ManagerOrders.as_view()(request)
#         self.assertEqual(response.status_code, 200)


# # class
# class TestManagerView(TransactionTestCase):
#         # def setUp(self):
#     client = Client()
#     # login = client.login(username='manager', password='adminadmin')
#     # self.manager_order =

#     def test_manager_login(self):
#         self.assertTrue(self.loginme)

#     # class TestMangerVews(TransactionTestCase):
#     #     def setUp(self):
#     #         self.client = Client()
#     #         self.user = User.objects.create_user(
#     #             'manager', 'manager@manager.com', 'managermanager')
#     #         self.user.is_staff = True
#     #         self.client.login(username='manager', password='managermanager')
