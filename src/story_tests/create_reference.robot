*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Books

*** Test Cases ***
At start there are no references
    Go To  ${HOME_URL}
    Title Should Be  Viitteidenhallinta
    Page Should Contain Link  Lisää uusi viite

After adding a reference, there is one
    Go To  ${HOME_URL}
    Click Link  Lisää uusi viite
    Set Title  test
    Set Author  test-author
    Set Year  2000
    Click Button  Create
    Page Should Contain  test, test-author, 2000

After adding two references, there are two
    Go To  ${HOME_URL}
    Click Link  Lisää uusi viite
    Set Title  test1
    Set Author  test-author
    Set Year  2001
    Click Button  Create
    Click Link  Lisää uusi viite
    Set Title  test2
    Set Author  author-test
    Set Year  2002
    Click Button  Create
    Page Should Contain  test1, test-author, 2001
    Page Should Contain  test2, author-test, 2002

*** Keywords ***
Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Author
    [Arguments]  ${author}
    Input Text  author  ${author}

Set Year
    [Arguments]  ${year}
    Input Text  year  ${year}