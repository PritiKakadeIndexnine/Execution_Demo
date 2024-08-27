*** Settings ***
Library  SeleniumLibrary
Variables     ../../PageObjects/Fixtures and Results/fixturesresults_locators.py
Resource    ../../Resources/Fixtures and Results/fixturesresults_keywords.robot
Resource    ../../Resources/Players/Players_Keywords.robot
Resource    ../../../../CommonBase/Web/Resources/Web_Common_Keywords.robot
Variables   ../../PageObjects/Players/Players_loacator.py
Variables   ../../PageObjects/Stats/stats_locator.py
Resource   ../../Resources/Stats/stats_keywords.robot
Variables   ../../PageObjects/Menu/Menu_locators.py

Test Setup      Launch Application
Test Teardown   Close Browser

*** Test Cases ***
TC95 Verify filter by skill as bowler
    [Tags]      Players
    Navigation Keyword    ${ipl_24_nav}  ${squad_page}  ${squad}


TC96 Verify filter by skill as allrounder
    [Tags]      Players
    Navigation Keyword    ${ipl_24_nav}  ${squad_page}  ${squad}


TC97 Verify filter by skill as wicketkeeper
    [Tags]      Players
    Navigation Keyword    ${ipl_24_nav}  ${squad_page}  ${squad}


TC98 Verify click on support staff tab
    [Tags]      Players
    Navigation Keyword    ${ipl_24_nav}  ${squad_page}  ${squad}

TC99 Verify redirection of all support staff to profile page
    [Tags]      Players     Demo
    Navigation Keyword    ${ipl_24_nav}  ${squad_page}  ${squad}
