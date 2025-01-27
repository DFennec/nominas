# Nominas
### Payroll management project built in TKinter with an embedded SQLite database to keep track of employees and their data,
### as well as to make a few basic statistics regarding employment within the company.
`Note: bear in mind that this project was built for a subject taught in Spanish and, as such, its menus are in Spanish.` 
<br>
<img align="left" alt="Nominas" width="1000px" src="https://github.com/DFennec/nominas/blob/master/Thumbnail.png?raw=true"/>
As it is apparent, the program has 4 main menus with its corresponding options. Below you may find a rundown of what each of these 4 menus do. Upon starting up the program, a check
will be carried out to look for the embedded database, if the program finds no local database, it will generate one of its own.
## ALTAS
  This menu acts as a form that allows the user to insert employees into the company's database.<br>
  
  ![image](https://github.com/user-attachments/assets/dfd9a91f-4a96-44c7-b8b1-405dc26aa45c)
  
  It features field validation to check the validity of the data into the fields NIF (ID  Number), Datos Bancarios (Bank Details), Número de Afiliación SS (Social Security Number). To filter and prevent invalid data, typos and basic forgery.
  #### Valid sample data:
  <br>
  
  ![image](https://github.com/user-attachments/assets/a9d4e932-73e4-4a3b-843f-387c9eb47be2)
  
  #### Invalid Data:
  <br>
  
  ![image](https://github.com/user-attachments/assets/be411c25-e94c-421f-b171-3351cfdec88e)
  
  Bundled in there is a script module to check the validity of the three fields called NIFNIECCModulo.py.<br>
## BAJAS
  This menu allows you to grant employees a leave. The fields will ask the user for the employee ID and the date in which the employee will have the leave.<br>
  
  ![image](https://github.com/user-attachments/assets/c5ef886e-89ef-4fde-b09e-05b92a6a0e98)

  It also features validation so that you can't grant a leave to an employee that is already on leave or that doesn't exist.
  #### Valid leave:
  <br>
  
  ![image](https://github.com/user-attachments/assets/7472b7eb-e792-4aac-b8ae-03cdd46db555)

  #### Invalid leave:
  <br>

  ![image](https://github.com/user-attachments/assets/e5a52d68-ea9c-45d0-82e6-21f0cc1110d7)

  <br>
  
## INFORMES
  This menu doesn't allow the user to interact with it, at least directly. It shows you some of the company employees' statistics.<br>

  ![image](https://github.com/user-attachments/assets/8aa6b1a8-db51-4614-bf7a-04ca551ff86f)

  Keep in mind this section won't work as intended if the company does not have at least one male and one female employee. 
  Rounding and other data treatment has been carried out when querying the database to make the report look more even. 
## NOMINAS
  In this section you can query the embedded database and calculate the payroll of the queried employee.<br>
  
  ![image](https://github.com/user-attachments/assets/5e552532-8a10-4ca7-836c-7405dc7b3ef0)

  Below the buttons of the UI are explained:
  
  ### CARGAR EMPLEADO

  It is used to load the employee ID details into the other fields. <br>
  
  ![image](https://github.com/user-attachments/assets/2c81d1de-ed05-4b3d-b487-c71c38667ed7)

  You can also load employees under leave. <br>

  ![image](https://github.com/user-attachments/assets/de93291e-f9f1-4b55-9054-4c3451074cf8)

  ### CALCULAR

  This button will calculate the payroll of the employee that is loaded.

  ![image](https://github.com/user-attachments/assets/a747d990-5d63-4d23-9b0c-c1c1ff7e96c7)

  It calculates wages according to the Income Tax Rate range in Spain in 2024, that spans from 0 to 47% depending on the gross income.
  As with all of the previous menus, it will prevent you from loading invalid data.

  #### Invalid input (ID 0):
  
  ![image](https://github.com/user-attachments/assets/b8af3a38-6367-4d3f-870d-edbd5f582d5e)
  
  #### Invalid input (no such employee ID):
  
  ![image](https://github.com/user-attachments/assets/b771e33c-199c-4c0f-8a5f-c583117ee804)
  
  ### IMPRIMIR

  This button will print out a pdf once the data is inserted and the payroll calculated.
  Admittedly, it is an extremely basic implementation and layout, as this was a non-required feature to earn bonus points.

  ![image](https://github.com/user-attachments/assets/61af9059-4b0c-4af1-971b-989907125c3f)

  ![image](https://github.com/user-attachments/assets/2a922d9a-da38-483c-9f5a-efc5c7cbc7a1)
