"""
 
:Project:        Test Project (<a href="">Give ref link and doc name</a>)<br/>
:Description:     Customer Data Management<br/>
:DB impact:       YES<br/>
:Commit inside:   NO<br/>
:Rollback inside: NO<br/>


"""

"""
creates an employee table
"""


CREATE SET TABLE EMPLOYEE( 
   EmployeeNo INTEGER, 
   FirstName VARCHAR(30), 
) 
UNIQUE PRIMARY INDEX ( EmployeeNo );



"""
Create a procedure 'InsertSalary'

        :param EmployeeNo: The employee number.
        :param Gross: The gross value.
        :param Deduction: The deduction value of particular employee.
        :param NetPay: Stores the net payment of an employee.        
"""
        

CREATE PROCEDURE InsertSalary ( 
   IN in_EmployeeNo INTEGER, IN in_Gross INTEGER, 
   IN in_Deduction INTEGER, IN in_NetPay INTEGER 
) 

"""
Inserts the table records into columns

:param EmployeeNo
:param Gross
:param Deduction
:param NetPay 


"""
BEGIN 
   INSERT INTO Salary ( 
      EmployeeNo, 
      Gross, 
      Deduction, 
      NetPay 
   ) 
   VALUES ( 
      :in_EmployeeNo, 
      :in_Gross, 
      :in_Deduction, 
      :in_NetPay 
   ); 