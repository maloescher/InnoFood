# Use cases

**Table of contents**

[TOC]
## Roles

| Role              | Description                                                  |
| ----------------- | ------------------------------------------------------------ |
| **Administrator** | Person that is responsible for creating and administrating cafes (assigning managers, changing contact data and info). |
| **Manager**       | Person, that fills in info about canteen(menu, if canteen is open or closed, etc.) and responses to the orders. |
| **Customer**          | Person which orders food.                                    |
## Use cases Testing
### Create order

| Use case name          | Create order                                                 |
| ---------------------- | :----------------------------------------------------------- |
| **Unique use case ID** | 007                                                          |
| **Primary actor(s)**   | Customer                                                         |
| **Brief description**  | Customer makes an order through the application                  |
| **Preconditions**      | The meals/dishes to be ordered are available                 |
| **Flow of events**     | 1. Customer selects the desired option from menu<br />2. Customer enters his location<br />3. Customer presses the submit button |
| **Postconditions**     | Order is completed                                           |

### Use Case Create order Testing

| Test Case name         | Create Order                                                 |               |                |
| ---------------------- | :----------------------------------------------------------- | ------------- | -------------- |
| **Test ID:**           | TC-1                                                         |               |                |
| **Test suite:**        | Create user order                                            |               |                |
| **Setup:**             | 1. Customer has logged in.                                   |               |                |
|                        |                                                              |               |                |
| **Teardown:**          | Send Customer order request to the server                    |               |                |
| **Step:**              | **Description**                                              | **Results**   | **Problem ID** |
| TC-1-A1                | Customer browses cafe list                                   | Passed        |                |
| TC-1-A2                | Customer selects cafe from menu                              | Passed        |                |
| TC-1-S3                | Application opens new page to correspoding cafe              | Passed        |                |
| TC-1-A4                | Customer browse menu                                         | Passed        |                |
| TC-1-A5                | Customer adds dihe(s) to cart by pressing cart icon          | Passed        |                |
| TC-1-A6                | Customer enters address                                      | Passed        |                |
| TC-1-A7                | Customer presses "Submit Orders" button                      | Passed        |                |
| TC-1-F8                | Oreder processed for delivery                                | Failed        | F1             |
| **Status:**            | **Failed**                                                   |               |                |
| **Tester:**            | All steps passed without any bug                             |               |                |
| **Date completed:**    | 28 November 2019                                             |               |                |
### Variables for TC - Create order
| **Type**    | **Name**    | **Value** |
| string      | destination | Innopolis |
| User object | user        | user1     |
| bool        | confirmed   | true      |
| Cafe object | cafe        | cafe2     |
### Delete order

| Use case name          | Delete order                                                         |
| ---------------------- | ------------------------------------------------------------         |
| **Unique use case ID** | 008                                                                  |
| **Primary actor(s)**   | Customer                                                             |
| **Brief description**  | Canceling order by Customer                                          |
| **Preconditions**      | Order is created less than 10 minutes ago                            |
| **Flow of events**     | 1. Customer selects his order<br />2. Customer presses delete button |
| **Postconditions**     | Order is deleted                                                     |

### Use Case Delete Order
| Test Case name         | Delete order                                                     |               |                |
| ---------------------- | :-----------------------------------------------------------     | ------------- | -------------- |
| **Test ID:**           | TC-2                                                             |               |                |
| **Test suite:**        | Delete Customer order                                            |               |                |
| **Setup**              | 1. Created user order                                            |               |                |
|                        | 2. Created Cafe object                                           |               |                |
|                        | 3. Created dish object                                           |               |                |
|                        | 4. Added dish(es) to user account                                |               |                |
| **Teardown**           | 1. Delete order from Customer order list                         |               |                |
|                        | 2. Save changes                                                  |               |                |
| **Step**               | **Description**                                                  | **Results**   | **Problem ID** |
| TC-2-A1                | Customer clicks "My Orders" from application manu                | Passed        |                |
| TC-2-S2                | Application responses customer order pages                       | Passed        |                |
| TC-2-A3                | Customer selects ordered dish(es) from list by pressing "X" icon | Passed        |                |
| TC-2-S4                | Application requests to server for choosen order                 | Passed        |                |
| TC-2-S5                | Server responds with updated dish list                           | Passed        |                |
| TC-2-F6                | System saves chages                                              | Failed        | F2             |
| **Status:**            | **Failed**                                                       |               |                |
| **Tester:**            | **All steps passed without any bug**                             |               |                |
| **Date Completed**     | **28 November 2019**                                             |               |                |


### Variables for TC -  create User
| **Type** | **Name** | **Value**   |
| string   | usename  | user        |
| string   | password | password123 |
| string   | email    | me@me.com   |
### Variables for TC -  create Manger
| **Type** | **Name** | **Value**        |
| string   | username | manager          |
| string   | password | mangeradmin      |
| string   | email    | manager@adim.com |
### Confirm order

| Use case name          | Confirm order                                                |
| ---------------------- | ------------------------------------------------------------ |
| **Unique use case ID** | 009                                                          |
| **Primary actor(s)**   | Manager                                                      |
| **Brief description**  | Manager confirms the order created by Customer                   |
| **Preconditions**      | Order is created by Customer                                     |
| **Flow of events**     | 1. Manager selects the pending order<br />2. Manager presses confirm button |
| **Postconditions**     | Order is confirmed                                           |

### Test Case Confirm order
| Test Case name         | Approve an order confirmation by manager                     |               |                |
| ---------------------- | :----------------------------------------------------------- | ------------- | -------------- |
| **Test ID:**           | TC-3                                                         |               |                |
| **Tes suite:**         | Confirm Order                                                |               |                |
| **Setup**              | 1. Create manager                                            |               |                |
|                        | 2. Login manager                                             |               |                |
|                        | 3. Create Order object                                       |               |                |
|                        | 4. Create Dish oject                                         |               |                |
|                        | 5. Add Dish to Order                                         |               |                |
| **Teardown**           | 1. Delete Manager                                            |               |                |
|                        | 2. Delete Oreder object                                      |               |                |
|                        | 3. Delete Dish object                                        |               |                |
| **Step**               | **Description**                                              | **Results**   | **Problem ID** |
|                        | 1. Manager clicks "active menu" from manager dahsboard       | Passed        |                |
|                        | 2. Application response page with list of active menu        | Passed        |                |
|                        | 3. Manger clicks "check" icon                                | Passed        |                |
|                        | 4. Application requests to server                            | Passed        |                |
|                        | 5. Server responds apdates list menu                         | Passed        |                |
|                        | 6. System saves changes                                      | Passed        |                |
| **Satus:**             | **Passed**                                                   |               |                |
| **Tester:**            | All step is passed without warning                           |               |                |
| **Date Completed**     | 28 November 2019                                             |               |                |


### Decline order

| Use case name          | Decline order                                                               |
| ---------------------- | ------------------------------------------------------------                |
| **Unique use case ID** | 010                                                                         |
| **Primary actor(s)**   | Manager                                                                     |
| **Brief description**  | Manager declines order                                                      |
| **Preconditions**      | Order is created by Customer                                                |
| **Flow of events**     | 1. Manager selects the pending order<br />2. Manager presses decline button |
| **Postconditions**     | Order is declined and deleted                                               |

### Use Case Decline order

| Test Case name         | Approve a decline of order by manager                        |               |                |
| ---------------------- | :----------------------------------------------------------- | ------------- | -------------- |
| **Test ID**            | TC-4                                                         |               |                |
| **Test Suite**         | 1. Create manager                                            |               |                |
|                        | 2. Login manager                                             |               |                |
|                        | 3. Create Order object                                       |               |                |
|                        | 4. Create Dish oject                                         |               |                |
|                        | 5. Add Dish to Order table                                   |               |                |
| **Teardown**           | 1. Delete Manager                                            |               |                |
|                        | 2. Delete Oreder object                                      |               |                |
|                        | 3. Delete Dish object                                        |               |                |
| **Step**               | **Description**                                              | **Results**   | **Problem ID** |
| TC-4-A1                | 1. Manager clicks "active menu" from manager dahsboard       | Passed        |                |
| TC-4-S2                | 2. Application response page with list of active menu        | Passed        |                |
| TC-4-A3                | 3. Manger clicks "X" icon                                    | Passed        |                |
| TC-4-S4                | 4. Application requests to server                            | Passed        |                |
| TC-4-S5                | 5. Server responds apdated list menu                         | Passed        |                |
| TC-4-s4                | 6. System saves changes                                      | Passed        |                |
| **Satus:**             | **Passed**                                                   |               |                |
| **Tester:**            | All step is passed without warning                           |               |                |
| **Date Completed**     | 28 November 2019                                             |               |                |

### Create dish

| Use case name          | Create dish                                                  |
| ---------------------- | ------------------------------------------------------------ |
| **Unique use case ID** | 011                                                          |
| **Primary actor(s)**   | Manager                                                      |
| **Brief description**  | Manager creates an entry in Menu table                       |
| **Preconditions**      | There is a Cafe entity that Manager is assigned to           |
| **Flow of events**     | 1. Manager opens the Menu table from his side<br />2. Manager presses 'Add' button<br />3. Pop-up window with the form containing name and price fields appears<br />4. Manager enters dish name<br />5. Manager enters dish price<br />6. Manager submits form<br />7. Database updates |
| **Postconditions**     | New Dish entry added into Menu table                         |

### Use Case Create dish

| Test Case name         | Approve creation of  dish  by manager                        |               |                |
| ---------------------- | :----------------------------------------------------------- | ------------- | -------------- |
| **Test ID**            | TC-5                                                         |               |                |
| **Test Suite**         | 1. Create manager                                            |               |                |
|                        | 2. Login manager                                             |               |                |
|                        | 3. Create cafe object from Cafe model                        |               |                |
| **Teardown**           | 1. Delete Manager                                            |               |                |
|                        | 2. Delete cafe object                                        |               |                |
| **Step**               | **Description**                                              | **Results**   | **Problem ID** |
| TC-5-A1                | 1. Manager clicks "Cafe" button from manager dahsboard       | Passed        |                |
| TC-5-S2                | 2. Application response page with list of cafe menu          | Passed        |                |
| TC-5-A3                | 3. Manger clikcs "Add dish" button                           | Passed        |                |
| TC-5-S4                | 4. Application open new page with form                       | Passed        |                |
| TC-5-A5                | 5. Manager fills form: dish name, price                      | Passed        |                |
| TC-5-A6                | 6. Manager presses "Save" button                             | Passed        |                |
| TC-5-S7                | 7. Application requests to server for dish form              | Passed        |                |
| TC-5-S8                | 8. System saves changes                                      | Passed        |                |
| TC-5-S9                | 9. Application redirects manager to "cafe" page              | Passed        |                |
| **Satus:**             | **Passed**                                                   |               |                |
| **Tester:**            | All step is passed without warning                           |               |                |
| **Date Completed**     | 28 November 2019                                             |               |                |

### Variables for TC - Create dish
| **Type**    | **Name** | **Value**    |
| string      | name     | dish1        |
| bool        | visible  | true         |
| Cage object | cafe     | Current cafe |

### Variables for TC -  create Cafe
| **Type**       | **Name** | **Value**  |
| string         | name     | name1      |
| string         | location | loacatoin1 |
| Manager object | manager  | manager1   |
| bool           | visible  | True       |
### Edit dish

| Use case name          | Edit dish                                                    |
| ---------------------- | ------------------------------------------------------------ |
| **Unique use case ID** | 012                                                          |
| **Primary actor(s)**   | Manager                                                      |
| **Brief description**  | Manager edits an entry in Menu table                         |
| **Preconditions**      | There are entries in the Menu table                          |
| **Flow of events**     | 1. Manager opens the Menu table from his side<br />2. Manager presses 'Edit' button<br />3. Pop-up window with the form containing name and price fields appears filled with the current values<br />4. Manager edits values<br />6. Manager submits form<br />7. Database updates |
| **Postconditions**     | Dish entry is updated                                        |

### Use Case Edit Dish

| Test Case name         | Approve editing dish by manager                                    |               |                |
| ---------------------- | :-----------------------------------------------------------       | ------------- | -------------- |
| **Test ID**            | TC-6                                                               |               |                |
| **Test Suite**         | 1. Create manager                                                  |               |                |
|                        | 2. Login manager                                                   |               |                |
|                        | 3. Create dish object from Dish model                              |               |                |
|                        | 3. Create cafe object from Cafe model                              |               |                |
|                        | 4. Add dish to cafe table                                          |               |                |
| **Teardown**           | 1. Delete Manager                                                  |               |                |
|                        | 2. Delete cafe object                                              |               |                |
|                        | 3. Delete dish object                                              |               |                |
| **Step**               | **Description**                                                    | **Results**   | **Problem ID** |
| TC-6-A1                | 1. Manager clicks "Cafe" button from manager dahsboard             | Passed        |                |
| TC-6-S2                | 2. Application response page with list of cafe menu available      | Passed        |                |
| TC-6-A3                | 3. Manger clikcs "Edit" icon from dish lish                        | Passed        |                |
| TC-6-S4                | 4. Application open new page with form: "update_dish" with dish id | Passed        |                |
| TC-6-A5                | 5. Manager updates form: dish name, price                          | Passed        |                |
| TC-6-A6                | 6. Manager presses "Save" button                                   | Passed        |                |
| TC-6-S7                | 7. Application requests for update to server for dish form         | Passed        |                |
| TC-6-S8                | 8. System saves changes                                            | Passed        |                |
| TC-6-S9                | 9. Application redirects manager to "cafe" page                    | Passed        |                |
| **Satus:**             | **Passed**                                                         |               |                |
| **Tester:**            | All step is passed without warning                                 |               |                |
| **Date Completed**     | 28 November 2019                                                   |               |                |

### Variables for TC - Edit dish
| **Type**    | **Name** | **Value**    |
| string      | name     | dish1        |
| Integer     | price    | 250          |
| bool        | visible  | true         |
| Cafe object | cafe     | current cafe |
### Edit menu

| Use case name          | Edit menu                                                    |
| ---------------------- | ------------------------------------------------------------ |
| **Unique use case ID** | 013                                                          |
| **Primary actor(s)**   | Manager                                                      |
| **Brief description**  | A manager sets available menu for each week                  |
| **Preconditions**      | There are entries in Menu table                              |
| **Flow of events**     | 1. Manager opens the Menu table from his side<br />2. Manger checks all of the check boxes next to entries setting their visibility for the Customer to True/False |
| **Postconditions**     | All of the unavailable meals are hidden from the Customer, all of the available are shown |
### NO implementation
### Create complaint

| Use case name          | Create complaint                                             |
| ---------------------- | ------------------------------------------------------------ |
| **Unique use case ID** | 014                                                          |
| **Primary actor(s)**   | Customer                                                         |
| **Brief description**  | If Customer is not satisfied, or unhappy with the order/delivery, he creates |
| **Preconditions**      | Order was confirmed by Manager                               |
| **Flow of events**     | 1. Customer presses 'Complain' button from home page<br />2. Customer enters Subject of the problem in the form<br />3. Customer enters description of the problem in the form<br />4. Customer enters his contact of the problem in the form<br />5. Customer submits the form to the system <br />3. Customer press home button |
| **Postconditions**     | Complaint is created and stored in the database              |

### Use case Create complaint

| Test Case name         | Approve editing dish by manager                                     |               |                |
| ---------------------- | :-----------------------------------------------------------        | ------------- | -------------- |
| **Test ID**            | TC-7                                                                |               |                |
| **Test Suite**         | 1. Create customer                                                  |               |                |
|                        | 2. Login customer                                                   |               |                |
|                        | 3. Create dish object from Dish model                               |               |                |
|                        | 3. Create cafe object from Cafe model                               |               |                |
|                        | 4. Add dish to cafe table                                           |               |                |
|                        | 5. Create order object from Order model                             |               |                |
|                        | 6. Create complaint object from Complaint model                     |               |                |
| **Teardown**           | 1. Delete Customer                                                  |               |                |
|                        | 2. Delete cafe object                                               |               |                |
|                        | 3. Delete dish object                                               |               |                |
|                        | 4. Delete complaint object                                          |               |                |
| **Step**               | **Description**                                                     | **Results**   | **Problem ID** |
| TC-7-A1                | 1. Customer clicks "Complaints" button from application header menu | Passed        |                |
| TC-7-S2                | 2. Application response page with complaint form                    | Passed        |                |
| TC-7-A3                | 3. Customer fills complaint form: Order number, Subject, Full       | Passed        |                |
|                        | complaint, Contact                                                  | Passed        |                |
| TC-7-A4                | 6. Customer presses "Submit" button                                 | Passed        |                |
| TC-7-S5                | 7. Application requests for update to server for complaint form     | Passed        |                |
| TC-7-S6                | 8. System saves changes                                             | Passed        |                |
| TC-7-S7                | 9. Application redirects manager to "home" page                     | Passed        |                |
| **Satus:**             | **Passed**                                                          |               |                |
| **Tester:**            | All step is passed without warning                                  |               |                |
| **Date Completed**     | 28 November 2019                                                    |               |                |


### Variables for TC - Create complaint
| **Type** | **Name**               | **Value**    |
| string   | destination            | Innopolis    |
| string   | complaint_title        | user1        |
| Integer  | complaint_order_number | 3            |
| string   | complaint_contact      | Current user |
| bool     | is_resolved            | false        |
### Resolve complaint

| Use case name          | Resolve complaint                                            |
| ---------------------- | ------------------------------------------------------------ |
| **Unique use case ID** | 015                                                          |
| **Primary actor(s)**   | Manager                                                      |
| **Brief description**  | When Manager contacted Customer outside the system, check in the system that the complaint is resolved |
| **Preconditions**      | Customer created complaint                                       |
| **Flow of events**     | 1. Manager see a list of un Resolved complains<br />2. Manager changes it's state to 'Resolved' py pressing on Resolve Button<br />3.Complain will be resolved and disappear from list|
| **Postconditions**     | Complaint is hidden from both Customer and manager               |

### Use Case Resolve complaint
| Test Case name         | Approve Resolving complaint by manager                           |               |                |
| ---------------------- | :-----------------------------------------------------------     | ------------- | -------------- |
| **Test ID**            | TC-8                                                             |               |                |
| **Test Suite**         | 1. Create manager                                                |               |                |
|                        | 2. Login manager                                                 |               |                |
|                        | 3. Create complaint object from Complaint model                  |               |                |
| **Teardown**           | 1. Delete Manager                                                |               |                |
|                        | 2. Delete complaint object                                       |               |                |
| **Step**               | **Description**                                                  | **Results**   | **Problem ID** |
| TC-8-A1                | 1. Manager clicks "Complaints" button from manager dahsboard     | Passed        |                |
| TC-8-S2                | 2. Application response page with list of complaint available    | Passed        |                |
| TC-8-A3                | 3. Manger clikcs "Check" icon on complaint from complaint list   | Passed        |                |
| TC-8-S4                | 7. Application requests for update complaint list                | Passed        |                |
| TC-8-S5                | 8. System saves changes                                          | Failed        | F3             |
| TC-8-S9                | 9. Application lists available complaint list to "complans" page | Passed        |                |
| **Satus:**             | **Passed**                                                       |               |                |
| **Tester:**            | All step is passed without warning                               |               |                |
| **Date Completed**     | 28 November 2019                                                 |               |                |


### Sign Up
	
| Use case name          | Sign Up                                                      |
| ---------------------- | ------------------------------------------------------------ |
| **Unique use case ID** | 016                                                          |
| **Primary actor(s)**   | Customer                                                     |
| **Brief description**  | Process where a customer create a new account to use the system. |
| **Preconditions**      | -                                                            |
| **Flow of events**     | 1. Customer is located in the home page. <br/> 2. Customer clic on "sing up" option <br/> 3. Customer fill the form with all the information required. <br/> 4. Customer click on submit buttom. <br/> 5. Customer reciebe a confirmation message. |
| **Alternative Flow **  | Customer does not receive confirmation message (error message). <br/> System display "Try again later" screen. |
| **Postconditions**     | A New Customer has been added to the database and is able to create new orders.<br/> |
| **Assumptions**        | The customer has a valid email acount. |
| **Non-behavioral requirements** | Changes must be visible for the customer without having to refresh the page. |


### Test Case Sign Up

| Test Case name         | Approve Application Sign up                                      |               |                |
| ---------------------- | :-----------------------------------------------------------     | ------------- | -------------- |
| **Test ID**            | TC-9                                                             |               |                |
| **Test Suite**         | 1. Create User                                                   |               |                |
| **Teardown**           | 1. Delete User                                                   |               |                |
| **Step**               | **Description**                                                  | **Results**   | **Problem ID** |
| TC-9-A1                | 1. Customer opens "Sign up" page                                 | Passed        |                |
| TC-9-A2                | 2. Customer fills sign up form: name, password, confirm password | Passed        |                |
| TC-9-A3                | 3. Customer presses "Sign Up" button                             | Passed        |                |
| TC-9-S4                | 4. Application redirects Customer to Sign in page                | Passed        |                |
| **Satus:**             | **Passed**                                                       |               |                |
| **Tester:**            | All step is passed without warning                               |               |                |
| **Date Completed**     | 28 November 2019                                                 |               |                |

### Variables for TC -  Signup Customer
| **Type** | **Name** | **Value**        |
| string   | username | test             |
| string   | password | 12test121        |
| string   | email    | test@example.com |

### Sign In

| Use case name          | Sign In                                                      |
| ---------------------- | ------------------------------------------------------------ |
| **Unique use case ID** | 017                                                          |
| **Primary actor(s)**   | Customer, Administrators, Managers                           |
| **Brief description**  | Sing in page to enter the system. Screen must be display acoording to user rights |
| **Preconditions**      | -                                                            |
| **Flow of events**     | 1. Actor is located in the home page. <br/> 2. Actor clic on "Sing in" option <br/> 3. Actor fill the user and password field <br/> 4. Actor click on "Sing in" butron <br/> <br/> 5. System validate actor credentials <br/> 6. System redirect actor to the home page depending on the actors rights on the system. |
| **Alternative Flow **  | Invalid credentials. <br/> Error message must be displayed. <br/> Actor has the option to reset the password. |
| **Postconditions**     | The actor access to the system |
| **Assumptions**        | - |
| **Non-behavioral requirements** | Changes must be visible for the actors without having to refresh the page. |

### Test Case Customer Sign In
| Test Case name         | Approve Application Sign in for Customer                     |               |                |
| ---------------------- | :----------------------------------------------------------- | ------------- | -------------- |
| **Test ID**            | TC-10                                                        |               |                |
| **Test Suite**         | 1. Create User                                               |               |                |
| **Teardown**           | 1. Delete User                                               |               |                |
| **Step**               | **Descriptioin**                                             | **Results**   | **Problem ID** |
| TC-10-A1               | 1. Customer opens "Sign in" page                             | Passed        |                |
| TC-10-A2               | 2. Customer fills sign up form: name, password field         | Passed        |                |
| TC-10-A3               | 3. Customer presses "Sign in" button                         | Passed        |                |
| TC-10-S4               | 4. Application post request to server with user data         | Passed        |                |
| TC-10-S5               | 5. Sever responses credentials for authenticated user        | Passed        |                |
| TC-10-S6               | 4. Application redirects Customer to home page               | Passed        |                |
| **Satus:**             | **Passed**                                                   |               |                |
| **Tester:**            | All step is passed without warning                           |               |                |
| **Date Completed**     | 28 November 2019                                             |               |                |


### Variables for TC -  Sigin Customer
| **Type** | **Name** | **Value**        |
| string   | username | test             |
| string   | password | 12test121        |
| string   | email    | test@example.com |
