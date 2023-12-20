# VMG1223
ViMiGo Assessment - NASRUL ARIF BIN ZAKRIA

## PART 1 - TECHNICAL

### PROGRESS A - ANALYSIS OF CASE STUDY

1. Problem statement:
- There are three services denoted as Service A, Service B and Service C.
- Service B and Service C are dependent to Service A.
- Thus, if there are any changes to Service A - maintenance must also be done to Service B and Service C.
- Hence, this will make the maintenance time and cost higher.
- What can be done for this case, to reduce the maintenance time and cost.

2. Possible solutions:
a) Using automated testing tools such as Selenium in which script can be written specifically for each Services.
b) Using an architecture / configuration in which functions are designed in such a way that when there is data / variable changes, will reflect other area that are related.

### PROGRESS B - POSSIBLE SOLUTIONS CLARIFICATION

[Click here](https://github.com/NasrulArif/VMG1223/blob/06a23a5b3b2a1a3cfaa17f799e407d21809dd22e/PART%203%20-%20FINAL%20SUBMISSION/Technical%20Assessment/Nasrul%20Arif%20-%20Technical%20Assessment.pdf) to view the documentation.

1. Using Automated Testing Tools
- Assuming that this case is developed in web and mobile platform.
- Thus we can use Selenium for web and Appium for mobile (Selenium based framework) to conduct automated testing.
- Selenium / Appium are automated testing tools that uses Python script for us to test a service and can be automated.
- During Testing phase of SDLC, Python test script will be written specifically for each service and only be modified when there are changes specifically for that service only.
- When there is a need to change a service that become dependencies to other services, similar test script still can be used to on every single service related.

2. Configuration Based Functions / End Points
- In this solution, we can imagine Laravel routes where it store URL / End Points in calling functions.
- A changes will only need to be done once and will be reflected as well in other services that call it.
- Another way is to store every API endpoints string in a single file that can be fetched by other services, thus when there are changes in the API endpoints string, less testing required unless the changes affect the data representation (datatype, formatting etc).

## PART 2 - WRITING

In this assessment, I have conducted research regarding Monolithic and Microservices architecture. [Click here](https://github.com/NasrulArif/VMG1223/blob/06a23a5b3b2a1a3cfaa17f799e407d21809dd22e/PART%203%20-%20FINAL%20SUBMISSION/Writing%20Assessment/Nasrul%20Arif%20-%20Writing%20Assessment.pdf) to view the proposal.
