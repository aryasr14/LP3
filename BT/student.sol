// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {

    // Structure to store student details
    struct Student {
        uint rollNo;
        string name;
        uint age;
        string department;
    }

    // Array to store multiple students
    Student[] public students;

    // Function to add student details
    function addStudent(
        uint _rollNo,
        string memory _name,
        uint _age,
        string memory _department
    ) public {
        students.push(Student(_rollNo, _name, _age, _department));
    }

    // Function to get student details
    function getStudent(uint index)
        public
        view
        returns (uint, string memory, uint, string memory)
    {
        Student memory s = students[index];

        return (s.rollNo, s.name, s.age, s.department);
    }

    // Function to get total number of students
    function getStudentCount() public view returns (uint) {
        return students.length;
    }

    // Fallback function
    fallback() external payable {
    }
}
