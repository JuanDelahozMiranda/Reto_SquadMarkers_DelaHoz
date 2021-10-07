from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import unittest
import time

class RetoQaSauceDemo(unittest.TestCase):
   
    @given(u'puedo ingresar al sitio web')
    def OpenBrowser(context):
        context.driver = webdriver.Chrome('./drivers/chromedriver.exe')
        context.driver.get('https://www.saucedemo.com/')
        context.driver.maximize_window()
        time.sleep(2)


    @when(u'presiono el boton de login')
    def PressButtonLogin(context):
        btnLogin = context.driver.find_element_by_xpath("//input[@type='submit']")
        btnLogin.click()


    @when(u'ingreso el campo usuario usando "{In_User}"')
    def TypeUser(context, In_User):
        txtUser = context.driver.find_element_by_xpath("//input[@id='user-name']")
        txtUser.send_keys(In_User)


    @when(u'ingreso el campo password usando "{In_Pass}"')
    def TypePassword(context, In_Pass):
        txtUser = context.driver.find_element_by_xpath("//input[@id='password']")
        txtUser.send_keys(In_Pass)


    @then(u'visualizo un mensaje de alerta como "{In_Message}"')
    def ShowMessage(context, In_Message):
        context.driver.implicitly_wait(1)
        lblError = context.driver.find_element_by_xpath("//h3[contains(text(),'Epic sadface:')]")
        assert lblError.text == In_Message    


    @then(u'verifico las imagenes con error')
    def verifyImagesWithError(context):
        lblTitulo = context.driver.find_element_by_xpath("//span[contains(@class, 'title')]")
        assert lblTitulo.text == 'PRODUCTS'

        elementFilter = context.driver.find_element_by_xpath("//*[contains(@class, 'product_sort_container')]").is_displayed()
        assert elementFilter is True

        elementImage = context.driver.find_element_by_xpath("//img[contains(@src, 'sl-404')]").is_displayed()
        assert elementImage is True


    @then(u'verifico las imagenes correctas')
    def verifyImagesSuccess(context):
        context.driver.implicitly_wait(7)
        
        lblTitulo = context.driver.find_element_by_xpath("//span[contains(@class, 'title')]")
        assert lblTitulo.text == 'PRODUCTS'

        elementFilter = context.driver.find_element_by_xpath("//*[contains(@class, 'product_sort_container')]").is_displayed()
        assert elementFilter is True

        elementImage2 = context.driver.find_element_by_xpath("//img[contains(@src, 'backpack')]").is_displayed()
        assert elementImage2 is True


    @then(u'Agrego un articulo al carrito')
    def AddItemtoCar(context):
        context.driver.implicitly_wait(2)
        context.driver.find_element_by_xpath("//button[@id='add-to-cart-sauce-labs-backpack']").click()
        context.driver.find_element_by_xpath("//*[contains(@class, 'shopping_cart_link')]").click()
        context.driver.implicitly_wait(2)


    @then(u'puedo visualizar el item seleccionado')
    def verifyItem_Page2(context):
        lblTitulo = context.driver.find_element_by_xpath("//span[contains(@class, 'title')]")
        assert lblTitulo.text == 'YOUR CART'
        
        lblArticulo = context.driver.find_element_by_xpath("//div[contains(@class, 'cart_item')]/div[contains(@class, 'cart_item_label')]/a/div")
        assert lblArticulo.text == 'Sauce Labs Backpack'

        lblPrecio = context.driver.find_element_by_xpath("//div[contains(@class, 'cart_item')]/div[contains(@class, 'cart_item_label')]/div[2]/div")
        assert lblPrecio.text == '$29.99'

        btnRemove = context.driver.find_element_by_xpath("//button[contains(@id, 'remove')]").is_displayed()
        assert btnRemove is True


    @then(u'presiono el boton checkout')
    def PressCheckoutButton(context):
        btnCheckout = context.driver.find_element_by_xpath("//button[@id='checkout']")
        btnCheckout.click()
        time.sleep(2)
    

    @then(u'Ingreso el "{In_Name}" junto con el "{In_LastName}" y un "{In_Code}"')
    def setUpInfoCostumer(context, In_Name, In_LastName, In_Code):
        lblTitulo = context.driver.find_element_by_xpath("//span[contains(@class, 'title')]")
        assert lblTitulo.text == 'CHECKOUT: YOUR INFORMATION'
        
        txtName = context.driver.find_element_by_xpath("//input[@id='first-name']")
        txtName.send_keys(In_Name)

        txtLastName = context.driver.find_element_by_xpath("//input[@id='last-name']")
        txtLastName.send_keys(In_LastName)

        txtCode = context.driver.find_element_by_xpath("//input[@id='postal-code']")
        txtCode.send_keys(In_Code)
        

    @then(u'presiono continuar')
    def PressContinue(context):
        btnContinue = context.driver.find_element_by_xpath("//input[@id='continue']")
        btnContinue.click()
        time.sleep(2)


    @then(u'visualizo un error con el mensaje "{In_Message}"')
    def ShowMessageError(context, In_Message):
        context.driver.implicitly_wait(1)
        lblError = context.driver.find_element_by_xpath("//h3[contains(text(),'Error:')]")
        assert lblError.text == In_Message
        

    @then(u'cierro la sesion')
    def LogOut(context):
        openMenu = context.driver.find_element_by_xpath("//button[@id='react-burger-menu-btn']")
        openMenu.click()
        context.driver.implicitly_wait(2)
        LogOutButton = context.driver.find_element_by_xpath("//a[@id='logout_sidebar_link']")
        LogOutButton.click()
        time.sleep(5)
        #closeMenu = context.driver.find_element_by_xpath("//button[@id='react-burger-cross-btn']")
        #closeMenu.click()


    @then(u'puedo visualizar la informacion de compra')
    def ShowTaxInfo(context):
        lblTitulo = context.driver.find_element_by_xpath("//span[contains(@class, 'title')]")
        assert lblTitulo.text == 'CHECKOUT: OVERVIEW'

        lblCard = context.driver.find_element_by_xpath("//div[contains(text(),'SauceCard')]").is_displayed()
        assert lblCard is True

        lblDelivery = context.driver.find_element_by_xpath("//div[contains(text(),'FREE PONY EXPRESS')]").is_displayed()
        assert lblDelivery is True

        lblItemPrice = context.driver.find_element_by_xpath("//div[contains(text(),'Item total')]").is_displayed()
        assert lblDelivery is True

        lblTax = context.driver.find_element_by_xpath("//div[contains(text(),'Tax')]").is_displayed()
        assert lblTax is True

        lblTotal = context.driver.find_element_by_xpath("//div[contains(text(),'Total')]").is_displayed()
        assert lblTotal is True


    @then(u'presino el boton finalizar')
    def PressFinishButton(context):
        FinishButton = context.driver.find_element_by_xpath("//button[@id='finish']")
        FinishButton.click()
        time.sleep(2)


    @then(u'visualizo confirmacion del pedido')
    def ShowSuccessOrder(context):
        lblTitulo = context.driver.find_element_by_xpath("//span[contains(@class, 'title')]")
        assert lblTitulo.text == 'CHECKOUT: COMPLETE!'

        lblconfirmOrder = context.driver.find_element_by_xpath("//h2[contains(text(),'THANK YOU FOR YOUR ORDE')]").is_displayed()
        assert lblconfirmOrder is True

        imgLogo = context.driver.find_element_by_xpath("//img[contains(@class,'pony_express')]").is_displayed()
        assert imgLogo is True