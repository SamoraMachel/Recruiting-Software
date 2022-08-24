

from dataclasses import dataclass
from typing import List

from app.db.Employee import Employee

@dataclass
class SearchCriteria: 
    skills: List[str] = None
    education: str = None
    tools: List[str] = None
    location: str = None
    pay_range: dict = None


class SearchController:
    SCORE_DIVISION = 20
    CRITERIA_COUNT = 5
    
    def __init__(self, search_str, search_criteria : SearchCriteria = None) -> None:
        self.employee_list : List[Employee] = Employee.readByValue("profession", [search_str])
        self.search_criteria = search_criteria
        self.score_employee()
    
    def __skills_filter_(self):
        skills_count = len(self.search_criteria.skills)
        for employee in self.employee_list:
            _skills_score = 0
            if employee.skills != None:
                for employee_skills in employee.skills:
                    if employee_skills in self.search_criteria.skills:
                        _skills_score += 1
            
            total_score = ((_skills_score/ skills_count) * self.SCORE_DIVISION) - ((6/ self.CRITERIA_COUNT) * self.SCORE_DIVISION)
            employee.score += total_score
    
    def __tools_filter_(self):
        tools_count = len(self.search_criteria.tools)
        for employee in self.employee_list:
            _tools_score = 0
            if employee.tools != None:
                for employee_tool in employee.tools:
                    if employee_tool in self.search_criteria.tools:
                        _tools_score += 1
            
            total_score = ((_tools_score/ tools_count) * self.SCORE_DIVISION) - ((3/ self.CRITERIA_COUNT) * self.SCORE_DIVISION)
            employee.score += total_score
            
    def __location_filter_(self):
        for employee in self.employee_list:
            _location_score = 0
            if employee.location != None :
                if employee.location == self.search_criteria.location:
                    _location_score = 1
            
            total_score = ((_location_score / 1) * self.SCORE_DIVISION) - ((4/ self.CRITERIA_COUNT) * self.SCORE_DIVISION)
            employee.score += total_score
    
    def __education_filter_(self):
        for employee in self.employee_list:
            _education_score = 0 
            if employee.education != None :
                for employee_education in employee.education:
                    education_title = employee_education.get("title", "")
                    if education_title == self.search_criteria.education:
                        _education_score = 1
            
            total_score = ((_education_score/ 1) * self.SCORE_DIVISION) - ((5/ self.CRITERIA_COUNT) * self.SCORE_DIVISION)
            employee.score += total_score
    
    def __pay_range_filter_(self):
        for employee in self.employee_list:
            _pay_range_score = 0
            if employee.pay_range != None:
                if self.search_criteria.pay_range.get("minimum", 0) > employee.pay_range.get("maximum", 0):
                    _pay_range_score = 5
                elif self.search_criteria.pay_range.get("maximum", 0) >= employee.pay_range.get("maximum", 0): 
                    _pay_range_score = 3

            total_score = ((_pay_range_score/ 5) * self.SCORE_DIVISION) - ((8/ self.CRITERIA_COUNT) * self.SCORE_DIVISION)
            employee.score += total_score

    
    def filter_data(self):
        if self.search_criteria.skills != None:
            self.__skills_filter_()
        if self.search_criteria.education != None:
            self.__education_filter_()
        if self.search_criteria.tools != None:
            self.__tools_filter_()
        if self.search_criteria.pay_range != None:
            self.__pay_range_filter_()
        if self.search_criteria.location != None:
            self.__location_filter_()
        return self.employee_list
    
    
    def score_employee(self):
        _employees = []
        for employee_object in self.employee_list:
            employee = Employee.toClassObject(employee_object)
            employee.score = 100
            _employees.append(employee)
        self.employee_list = _employees


