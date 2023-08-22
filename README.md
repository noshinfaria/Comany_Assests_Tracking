# Comany_Assests_Tracking
It's a DRF project of tracking assets (phones, tablets, laptops and other gear) handed out to employees.

# Requirement.txt file is included: https://github.com/noshinfaria/Comany_Assests_Tracking/blob/main/requirements.txt


# Operators:
- Create a new company (Authentication isn't required; Placeholder included for subscription)
- Register Staff ( A staff can register only under a company )
- Create a new Employee (Authentication required, staff can assign new employees)
- Create a new Device (Authentication required, staff can assign new devices)
- Create a new Devicelog (Authentication required, staff can assign new devices)




# Server run:

    - command: python manage.py runserver `127.0.0.1:8000`

## Commands

- python -m pip install -r requirements.txt
- python version: ```3.8.5```
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver



