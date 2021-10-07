#language: en
Feature: El usuario puede interactuar en el sitio web y comprar productos
  Como usuario puedo ingresar al sito Web de SauceDemo
  Despues de ingresar usando un usuario con permisos
  y seleccionar un producto
  Puedo agregarlo al carrito
  Tambien puedo finalizar el proceso de compra

  Background: common steps
    Given puedo ingresar al sitio web

  @negative
  Scenario: Como usuario ingreso al sitio web pero dejo los campos vacios
    When presiono el boton de login
    Then visualizo un mensaje de alerta como "Epic sadface: Username is required"

  @negative
  Scenario: Como usuario ingreso al sitio web y solo digito el usuario
    When ingreso el campo usuario usando "In_data"
    When presiono el boton de login
    Then visualizo un mensaje de alerta como "Epic sadface: Password is required"

  @negative
  Scenario: Como usuario ingreso al sitio web y solo digito la contrasena
    When ingreso el campo password usando "In_data"
    When presiono el boton de login
    Then visualizo un mensaje de alerta como "Epic sadface: Username is required"

  @negative
  Scenario: Como usuario ingreso al sitio web utilizando credenciales no validas
    When ingreso el campo usuario usando "In_data"
    When ingreso el campo password usando "In_data"
    When presiono el boton de login
    Then visualizo un mensaje de alerta como "Epic sadface: Username and password do not match any user in this service"

  @user-locked @positive
  Scenario: Como usuario ingreso al sitio web utilizando credenciales BLOQUEADAS
    When ingreso el campo usuario usando "locked_out_user"
    When ingreso el campo password usando "secret_sauce"
    When presiono el boton de login
    Then visualizo un mensaje de alerta como "Epic sadface: Sorry, this user has been locked out."

  @user-problem
  Scenario: Como usuario ingreso al sitio web utilizando credenciales validas pero la plataforma falla 
    When ingreso el campo usuario usando "problem_user"
    When ingreso el campo password usando "secret_sauce"
    When presiono el boton de login
    Then verifico las imagenes con error
    And Agrego un articulo al carrito
    Then puedo visualizar el item seleccionado
    And presiono el boton checkout
    And Ingreso el "nombre" junto con el "apellido" y un "codigo"
    And presiono continuar
    Then visualizo un error con el mensaje "Error: Last Name is required"
    And cierro la sesion

  @user-standard @positive
  Scenario: Como usuario ingreso al sitio web, agrego un elemento al carrito y finalizo la compra exitosamente
    When ingreso el campo usuario usando "standard_user"
    When ingreso el campo password usando "secret_sauce"
    When presiono el boton de login
    Then verifico las imagenes correctas
    And Agrego un articulo al carrito
    Then puedo visualizar el item seleccionado
    And presiono el boton checkout
    And Ingreso el "Juan" junto con el "DelaHoz" y un "080001"
    And presiono continuar
    Then puedo visualizar la informacion de compra
    And presino el boton finalizar
    Then visualizo confirmacion del pedido
    And cierro la sesion

  @performance_glitch_user @positive
  Scenario: Como usuario ingreso al sitio web utilizando credenciales validas pero no avanzo al checkout
    When ingreso el campo usuario usando "performance_glitch_user"
    When ingreso el campo password usando "secret_sauce"
    When presiono el boton de login
    Then verifico las imagenes correctas
    And Agrego un articulo al carrito
    Then puedo visualizar el item seleccionado
    And presiono el boton checkout
    And Ingreso el "Juan" junto con el "DelaHoz" y un "080001"
    And presiono continuar
    Then puedo visualizar la informacion de compra
    And presino el boton finalizar
    Then visualizo confirmacion del pedido
    And cierro la sesion