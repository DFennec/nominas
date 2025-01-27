# Nominas
### Payroll management project built in TKinter with an embedded SQLite database to keep track of employees and their data, as well as to make a few basic statistics regarding employment within the company.
`Note: bear in mind that this project was built for a subject taught in Spanish and, as such, its menus are in Spanish.` <br>
<img align="left" alt="Nominas" width="1000px" src="https://github.com/DFennec/nominas/blob/master/Thumbnail.png?raw=true"/>
As it is apparent, the program has 4 main menus with its corresponding options. Below you may find a rundown of what each of these 4 menus do.
## ALTAS
  This menu acts as a form that allows the user to insert employees into the company's database.<br>
  
  ![image](https://github.com/user-attachments/assets/dfd9a91f-4a96-44c7-b8b1-405dc26aa45c)
  
  It features field validation to check the validity of the data into the fields NIF (ID  Number), Datos Bancarios (Bank Details), Número de Afiliación SS (Social Security Number). To filter and prevent invalid data, typos and basic forgery.
  ### Valid sample data:
  <br>
  
  ![image](https://github.com/user-attachments/assets/a9d4e932-73e4-4a3b-843f-387c9eb47be2)
  
  ### Invalid Data:
  <br>
  
  ![image](https://github.com/user-attachments/assets/be411c25-e94c-421f-b171-3351cfdec88e)
  
  Bundled in there is a script module to check the validity of the three fields called NIFNIECCModulo.py.<br>
## BAJAS
  This menu allows you to grant employees a leave. The fields will ask the user for the employee ID and the date in which the employee will have the leave.<br>
  
  ![image](https://github.com/user-attachments/assets/c5ef886e-89ef-4fde-b09e-05b92a6a0e98)

  It also features validation so that you can't grant a leave to an employee that is already on leave or that doesn't exist.
  ### Valid leave:
  <br>
  
  ![image](https://github.com/user-attachments/assets/7472b7eb-e792-4aac-b8ae-03cdd46db555)

  ### Invalid leave:
  <br>

  ![image](https://github.com/user-attachments/assets/e5a52d68-ea9c-45d0-82e6-21f0cc1110d7)

  <br>
  
## INFORMES
  This menu acts as a form that allows the user to insert employees into the company database.<br>
  
## NOMINAS
  This menu acts as a form that allows the user to insert employees into the company database.<br>
  
