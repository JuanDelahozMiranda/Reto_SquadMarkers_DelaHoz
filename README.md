# Reto_SquadMarkers_DelaHoz
# DelaHozMiranda_JuanPablo
QA_Web_Testing_Python

## General Info
- Python version 3.10.0

## STEPS - API
1. Clone the repository
2. Check the dependencies

    2.1 - pip install selenium
 
    2.2 - pip install unittest2
    
    2.3 - pip install behave
    
    2.4 - pip install allure-behave

3. Verify your version chromedriver an located in [resources/drivers]
4. Check the scenarios [resources/testWeb.feature]
5. Execution -> navigate into resource folder and used: behave testWeb.feature
6. To run and generate report in json format used: behave -f allure_behave.formatter:AllureFormatter -o reports/ 
7. Check the summary reports In folder: [resources/reports/*.json]
