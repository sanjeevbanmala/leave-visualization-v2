import typing as ty
from typing import Optional, Dict
from datetime import date, datetime

from pydantic import BaseModel, EmailStr


class LeaveEventSchema(BaseModel):
    id: int
    userId: int
    empId: str
    designationId: int
    designationName: str
    firstName: str
    middleName: ty.Optional[str]
    lastName: str
    email: str
    departmentDescription: str
    startDate: date
    endDate: date
    leaveDays: int
    reason: str
    status: str
    leaveTypeId: int
    leaveType: str
    defaultDays: int
    transferableDays: int
    fiscalId: int
    fiscalStartDate: datetime
    fiscalEndDate: datetime
    fiscalIsCurrent: bool
    createdAt: datetime
    updatedAt: Optional[datetime]


class ImportedLeaveInformationSchema(BaseModel):
    userId: int
    empId: str
    teamManagerId: Optional[int]
    designationId: int
    designationName: str
    firstName: str
    middleName: Optional[str]
    lastName: str
    email: str
    isHr: bool
    isSupervisor: bool
    leaveIssuerId: Optional[int]
    issuerFirstName: Optional[str]
    issuerMiddleName: Optional[str]
    issuerLastName: Optional[str]
    currentLeaveIssuerId: Optional[int]
    currentLeaveIssuerEmail: Optional[str]
    departmentDescription: str
    startDate: date
    endDate: date
    leaveDays: int
    reason: str
    leaveStatus: str
    status: str
    responseRemarks: Optional[str]
    leaveTypeId: int
    leaveType: str
    defaultDays: int
    transferableDays: int
    isConsecutive: int
    fiscalId: int
    fiscalStartDate: datetime
    fiscalEndDate: datetime
    fiscalIsCurrent: bool
    createdAt: datetime
    updatedAt: Optional[datetime]
    isAutomated: int
    isConverted: int
    totalCount: int
    allocations: Optional[list[Dict]]

    class Config:
        orm_mode = True