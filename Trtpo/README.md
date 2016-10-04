# **Requirements Document** 
## 1. Introduction  

>The name of the project is _**“STBarbershop”**_. This product is intended for **fast enrollment** for all people, who need barbershop’s services. Also it helps to **simplify work process** for employees by looking through their personal schedule.  
>There are some abilities for registed clients such as their personal statistics of barbershop visits, email notifications, leaving comments about barbershop.

## 2. User Requirements
### Software Interfaces  
* Frameworks:
	* Ruby on Rails (v. 5.0)
	* Bootstrap (v. 3)
* Database modules:
	* PostgreSQL
* Hosting:
	* Heroku
* Programming languages: 
	* Ruby
	* Java Script
	
### 2.2 User Interfaces
User interfaces are presented in mockup directory.
### 2.3 User Characteristics
Web-site is intended for:
1) Not-registered clients.
2) Registered clients.
3) Employees.
4) Admin.  
### 2.4 Assumptions and Dependencies
Client can enroll during all day and night.

## 3. System Requirements
### 3.1 Functional Requirements
__The project will have such options as:__  
* Registration/Authorization:
	* By email and password with email confirmation;
* Abilities for not-registered clients:
	* Read all information about barbershop.
	* Can enroll.
* Abilities for registered clients:
	* Personal cabinet with:
		* Personal info(Name, Phone, etc.).
		* Personal statistics of visits.
		* Settings to personal info.
	* Email notifications about haircuts.
* Employees abilities:
	* Personal cabinet with:
		* Personal info(Name, Phone, etc.).
		* Work schedule.
		* Settings to personal info.
	* Can add new clients to schedule.
	* Checking clients visiting.
* Admin abilities:
	* Can block, delete clients.
	* Can add, delete employees.
	* Can add, edit content of whole site.

### 3.2 Non-Functional Requirements
#### 3.2.1 SOFTWARE QUALITY ATTRIBUTES
* Responsive web design.
* Result more than 80% of Google PageSpeed for all devices.
* Fast processing of clients request.


