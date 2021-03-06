*** Settings ***
Library  SeleniumLibrary

Suite Teardown  Close Browser

*** Variables ***
${USER OPENCART URL}            http://192.168.102.98/opencart/admin/
${BROWSER}                      Firefox
${USER NAME}                    support
${PASSWORD}                     elephant
${USER NAME FIELD}              id:input-username
${PASSWORD FIELD}               id:input-password
${ACCEPT LOGIN BUTTON}          xpath://button[@type='submit']
${CLOSE ALERT}                  xpath://button[@class='close']
${CONTENT FIELD}                id:content
${CATALOG BUTTON}               id:menu-catalog
${PRODUCTS BUTTON}              link:Products
${FILTER NAME}                  id:input-name
${FILTER BUTTON}                id:button-filter
${PRODUCT TABLE}                id:form-product
${ADD PRODUCT BUTTON}           xpath://a[@data-original-title='Add New']
${NEW PRODUCT NAME}             id:input-name1
${META TAG}                     id:input-meta-title1
${DATA TAB}                     xpath://a[@href='#tab-data']
${MODEL FILED}                  id:input-model
${SAVE NEW PRODUCT}             xpath://button[@data-original-title='Save']
${CHOOSE PRODUCTS}              xpath://input[@onclick="$('input[name*=\'selected\']').prop('checked', this.checked);"]
${REMOVE BUTTON}                xpath://button[@data-original-title='Delete']
${LOGOUT BUTTON}                xpath://a[@href='http://192.168.102.98/opencart/admin/index.php?route=common/logout&user_token=CdrybExkOhbxdqaEELoob2TnrP3VPp7l']

*** Keywords ***
Open user opencart
    Open Browser                url=${USER OPENCART URL}
    ...                         browser=${BROWSER}
Login opencart
    Input Text                  locator=${USER NAME FIELD}
    ...                         text=${USER NAME}
    Input Password              locator=${PASSWORD FIELD}
    ...                         password=${PASSWORD}
    Click Element               locator=${ACCEPT LOGIN BUTTON}
    Click Element               locator=${CLOSE ALERT}

Add product
    Click Element               locator=${CATALOG BUTTON}
    Click Element               locator=${PRODUCTS BUTTON}
    Click Element               locator=${ADD PRODUCT BUTTON}
    Input Text                  locator=${NEW PRODUCT NAME}
    ...                         text=Test Product
    Input Text                  locator=${META TAG}
    ...                         text=Test Tag
    Click Element               locator=${DATA TAB}
    Input Text                  locator=${MODEL FILED}
    ...                         text=Test Model
    Click Element               locator=${SAVE NEW PRODUCT}

Remove product
    Click Element               locator=${CHOOSE PRODUCTS}
    Click Element               locator=${REMOVE BUTTON}
    Alert Should Be Present     action=ACCEPT

*** Test Cases ***
Login into opencart
    Open user opencart
    Input Text                  locator=${USER NAME FIELD}
    ...                         text=${USER NAME}
    Input Password              locator=${PASSWORD FIELD}
    ...                         password=${PASSWORD}
    Click Element               locator=${ACCEPT LOGIN BUTTON}
    Click Element               locator=${CLOSE ALERT}
    Table Should Contain        locator=${CONTENT FIELD}
    ...                         expected=Dashboard

Filter product
    Open user opencart
    Login opencart
    Click Element               locator=${CATALOG BUTTON}
    Click Element               locator=${PRODUCTS BUTTON}
    Input Text                  locator=${FILTER NAME}
    ...                         text=Apple Cinema 30"
    Click Element               locator=${FILTER BUTTON}
    Table Should Contain        locator=${PRODUCT TABLE}
    ...                         expected=Apple Cinema 30"

Add product
    Open user opencart
    Login opencart
    Click Element               locator=${CATALOG BUTTON}
    Click Element               locator=${PRODUCTS BUTTON}
    Click Element               locator=${ADD PRODUCT BUTTON}
    Input Text                  locator=${NEW PRODUCT NAME}
    ...                         text=Test Product
    Input Text                  locator=${META TAG}
    ...                         text=Test Tag
    Click Element               locator=${DATA TAB}
    Input Text                  locator=${MODEL FILED}
    ...                         text=Test Model
    Click Element               locator=${SAVE NEW PRODUCT}
    Input Text                  locator=${FILTER NAME}
    ...                         text=Test Product
    Click Element               locator=${FILTER BUTTON}
    Table Should Contain        locator=${PRODUCT TABLE}
    ...                         expected=Test Product
    Remove product

Remove product
    Open user opencart
    Login opencart
    Add product
    Input Text                  locator=${FILTER NAME}
    ...                         text=Test Product
    Click Element               locator=${FILTER BUTTON}
    Click Element               locator=${CHOOSE PRODUCTS}
    Click Element               locator=${REMOVE BUTTON}
    Alert Should Be Present     action=ACCEPT
    Input Text                  locator=${FILTER NAME}
    ...                         text=Test Product
    Page Should Not Contain     text=Text Product

Logout
    Open user opencart
    Login opencart
    Click Element               locator=${LOGOUT BUTTON}
    Table Should Contain        locator=${CONTENT FIELD}
    ...                         expected=Please enter your login details.
