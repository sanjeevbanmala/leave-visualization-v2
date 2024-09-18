from sqlalchemy import Column, ForeignKey, UniqueConstraint, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import Boolean, Date, DateTime, Integer, String, JSON, Text

from models.partial_columns import NotNullColumn

Base = declarative_base()


class ImportedLeaveInformation(Base):
    __tablename__ = "imported_leave_information"
    __table_args__ = {"schema": "raw"} 

    id = Column(Integer, primary_key=True)
    userId = Column(Integer)
    empId = Column(String)
    teamManagerId = Column(Integer)
    designationId = Column(Integer)
    designationName = Column(String)
    firstName = Column(String)
    middleName = Column(String, nullable=True)
    lastName = Column(String)
    email = Column(String)
    isHr = Column(Boolean)
    isSupervisor = Column(Boolean)
    leaveIssuerId = Column(Integer)
    issuerFirstName = Column(String)
    issuerMiddleName = Column(String, nullable=True)
    issuerLastName = Column(String)
    currentLeaveIssuerId = Column(Integer)
    currentLeaveIssuerEmail = Column(String)
    departmentDescription = Column(Text)
    startDate = Column(Date)
    endDate = Column(Date)
    leaveDays = Column(Integer)
    reason = Column(Text)
    leaveStatus = Column(String)
    status = Column(String)
    responseRemarks = Column(Text, nullable=True)
    leaveTypeId = Column(Integer)
    leaveType = Column(String)
    defaultDays = Column(Integer)
    transferableDays = Column(Integer)
    isConsecutive = Column(Integer)
    fiscalId = Column(Integer)
    fiscalStartDate = Column(DateTime)
    fiscalEndDate = Column(DateTime)
    fiscalIsCurrent = Column(Boolean)
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)
    isAutomated = Column(Integer)
    isConverted = Column(Integer)
    totalCount = Column(Integer)
    allocations = Column(JSON, nullable=True)

class DboImportedLeaveInformation(Base):
    __tablename__ = "imported_leave_information"
    __table_args__ = {"schema": "dbo"} 

    id = NotNullColumn(Integer, primary_key=True)
    userId = NotNullColumn(Integer)
    empId = NotNullColumn(String(length=255))
    teamManagerId = Column(Integer)
    designationId = NotNullColumn(Integer)
    designationName = NotNullColumn(String(length=255))
    firstName = NotNullColumn(String(length=255))
    middleName = Column(String, nullable=True)
    lastName = NotNullColumn(String(length=255))
    email = NotNullColumn(String(length=255))
    isHr = NotNullColumn(Boolean)
    isSupervisor = NotNullColumn(Boolean)
    leaveIssuerId = Column(Integer)
    issuerFirstName = Column(String(length=255))
    issuerMiddleName = Column(String, nullable=True)
    issuerLastName = Column(String(length=255))
    currentLeaveIssuerId = Column(Integer)
    currentLeaveIssuerEmail = Column(String(length=255))
    departmentDescription = NotNullColumn(Text)
    startDate = NotNullColumn(Date)
    endDate = NotNullColumn(Date)
    leaveDays = NotNullColumn(Integer)
    reason = NotNullColumn(Text)
    leaveStatus = NotNullColumn(String(length=255))
    status = NotNullColumn(String(length=255))
    responseRemarks = Column(Text, nullable=True)
    leaveTypeId = NotNullColumn(Integer)
    leaveType = NotNullColumn(String(length=255))
    defaultDays = NotNullColumn(Integer)
    transferableDays = NotNullColumn(Integer)
    isConsecutive = NotNullColumn(Integer)
    fiscalId = NotNullColumn(Integer)
    fiscalStartDate = NotNullColumn(DateTime)
    fiscalEndDate = NotNullColumn(DateTime)
    fiscalIsCurrent = NotNullColumn(Boolean)
    createdAt = NotNullColumn(DateTime)
    updatedAt = Column(DateTime)
    isAutomated = NotNullColumn(Integer)
    isConverted = NotNullColumn(Integer)
    totalCount = NotNullColumn(Integer)
    allocations = Column(JSON, nullable=True)


class DboAllocations(Base):
    __tablename__ = "allocations"
    __table_args__ = {"schema": "dbo"}

    allocation_id = NotNullColumn(Integer, primary_key=True)
    name = NotNullColumn(String(length=100))
    type = Column(String(length=100))



class DboDesignations(Base):
    __tablename__ = "designations"
    __table_args__ = {"schema": "dbo"}

    designation_id = NotNullColumn(Integer, primary_key=True)
    designation_name = NotNullColumn(String(length=100))


class DboTeamManagers(Base):
    __tablename__ = "team_managers"
    __table_args__ = {"schema": "dbo"}

    team_manager_id = NotNullColumn(Integer, primary_key=True)
    name = Column(String(length=100), nullable=True)

class DboDepartments(Base):
    __tablename__ = "departments"
    __table_args__ = {"schema": "dbo"}

    department_id = NotNullColumn(Integer, primary_key=True, autoincrement=True)
    department_name = NotNullColumn(String(length=100), unique=True)


class DboLeaveIssuer(Base):
    __tablename__ = "leave_issuer"
    __table_args__ = {"schema": "dbo"}

    leave_issuer_id = NotNullColumn(Integer, primary_key=True)
    first_name = Column(String(length=100), nullable=True)
    last_name = Column(String(length=100), nullable=True)
    email = Column(String(length=100), nullable=True)


class DboLeaveTypes(Base):
    __tablename__ = "leave_types"
    __table_args__ = {"schema": "dbo"}

    leave_type_id = NotNullColumn(Integer, primary_key=True)
    leave_type = NotNullColumn(String(length=100))
    default_days = NotNullColumn(Integer)
    transferrable_days = NotNullColumn(Integer)


class DboFiscalYear(Base):
    __tablename__ = "fiscal_year"
    __table_args__ = {"schema": "dbo"}

    fiscal_id = NotNullColumn(Integer, primary_key=True)
    start_date = NotNullColumn(Date)
    end_date = NotNullColumn(Date)


class DboEmployees(Base):
    __tablename__ = "employees"
    __table_args__ = {"schema": "dbo"}

    employee_id = NotNullColumn(Integer, primary_key=True)
    first_name = NotNullColumn(String(length=100))
    middle_name = Column(String(length=100), nullable=True)
    last_name = NotNullColumn(String(length=100))
    email = NotNullColumn(String(length=100))
    is_hr = NotNullColumn(Boolean)
    is_supervisor = NotNullColumn(Boolean)
    designation_id = NotNullColumn(Integer, ForeignKey("dbo.designations.designation_id"))
    team_manager_id = Column(Integer, nullable=True)
    department_id = NotNullColumn(Integer, ForeignKey("dbo.departments.department_id"))

   
class DboEmployeeAllocations(Base): 
    __tablename__ = "employee_allocations"

    employee_id = NotNullColumn(Integer, ForeignKey("dbo.employees.employee_id"))
    allocation_id = NotNullColumn(Integer, ForeignKey("dbo.allocations.allocation_id"))

    __table_args__ = (
        PrimaryKeyConstraint('employee_id', 'allocation_id'),
        {'schema': 'dbo'} 
    )


class DboEmployeeLeaveIssuer(Base):
    __tablename__ = "employee_leave_issuer"
    
    employee_id = NotNullColumn(Integer, ForeignKey("dbo.employees.employee_id"))
    leave_issuer_id = Column(Integer, nullable=True)
    is_current_leave_issuer= NotNullColumn(Boolean)

    __table_args__ = (
        PrimaryKeyConstraint('employee_id', 'leave_issuer_id'),
        {'schema': 'dbo'} 
    )



class DboEmployeeLeaves(Base):
    __tablename__ = "employee_leaves"
    __table_args__ = {"schema": "dbo"}

    leave_id = NotNullColumn(Integer, primary_key=True)
    leave_issuer_id = NotNullColumn(Integer)
    leave_type_id = NotNullColumn(Integer, ForeignKey("dbo.leave_types.leave_type_id"))
    employee_id = NotNullColumn(Integer, ForeignKey("dbo.employees.employee_id"))
    fiscal_id = NotNullColumn(Integer, ForeignKey("dbo.fiscal_year.fiscal_id"))
    leave_days = NotNullColumn(Integer)
    reason = NotNullColumn(Text)
    status = NotNullColumn(String(length=100))
    remarks = Column(Text, nullable=True)
    is_consecutive= NotNullColumn(Boolean)
    start_date = NotNullColumn(Date)
    end_date = NotNullColumn(Date)
    created_at = NotNullColumn(DateTime)
    updated_at = Column(DateTime, nullable=True)

__all__ = [
    "Base",
    "ImportedLeaveInformation",
    "DboImportedLeaveInformation",
    "DboAllocations",
    "DboDesignations",
    "DboTeamManagers",
    "DboDepartments",
    "DboLeaveIssuer",
    "DboLeaveTypes",
    "DboFiscalYear",
    "DboEmployees",
    "DboEmployeeAllocations",
    "DboEmployeeLeaveIssuer",
    "DboEmployeeLeaves",
]
