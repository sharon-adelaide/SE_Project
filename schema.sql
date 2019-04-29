DROP DATABASE IF EXISTS ASHCROWDCOUNT;
CREATE DATABASE ASHCROWDCOUNT;
USE ASHCROWDCOUNT;

CREATE TABLE IF NOT EXISTS ROOMINFORMATION (
    LectureRoom VARCHAR(255),
    Occupancy INT,
    AirQualityLevel DECIMAL(3,2),
    PRIMARY KEY (LectureRoom));  
    
 INSERT INTO ROOMINFORMATION (LectureRoom, Occupancy, AirQualityLevel) VALUES ('Lab 221', 0, 0.1);                        
 INSERT INTO ROOMINFORMATION (LectureRoom, Occupancy, AirQualityLevel) VALUES ('Lab 222', 0, 0.1);
 INSERT INTO ROOMINFORMATION (LectureRoom, Occupancy, AirQualityLevel) VALUES ('RB 100', 0, 0.1);                                                                                    
 INSERT INTO ROOMINFORMATION (LectureRoom, Occupancy, AirQualityLevel) VALUES ('RB 115', 0, 0.1);   
 INSERT INTO ROOMINFORMATION (LectureRoom, Occupancy, AirQualityLevel) VALUES ('RB 216', 0, 0.1);
 INSERT INTO ROOMINFORMATION (LectureRoom, Occupancy, AirQualityLevel) VALUES ('King 202', 0, 0.1);  
 INSERT INTO ROOMINFORMATION (LectureRoom, Occupancy, AirQualityLevel) VALUES ('King 204', 0, 0.1);
 INSERT INTO ROOMINFORMATION (LectureRoom, Occupancy, AirQualityLevel) VALUES ('JH 115', 0, 0.1);
 INSERT INTO ROOMINFORMATION (LectureRoom, Occupancy, AirQualityLevel) VALUES ('JH 116', 0, 0.1);
 INSERT INTO ROOMINFORMATION (LectureRoom, Occupancy, AirQualityLevel) VALUES ('AH 216', 0, 0.1);
 INSERT INTO ROOMINFORMATION (LectureRoom, Occupancy, AirQualityLevel) VALUES ('AH 217', 0, 0.1);        
 INSERT INTO ROOMINFORMATION (LectureRoom, Occupancy, AirQualityLevel) VALUES ('DFH 218', 0, 0.1);
 INSERT INTO ROOMINFORMATION (LectureRoom, Occupancy, AirQualityLevel) VALUES ('MPR', 0, 0.1);      
INSERT INTO ROOMINFORMATION (LectureRoom, Occupancy, AirQualityLevel) VALUES ('NM 207A', 0, 0.1); 
INSERT INTO ROOMINFORMATION (LectureRoom, Occupancy, AirQualityLevel) VALUES ('NM 207B', 0, 0.1); 
INSERT INTO ROOMINFORMATION (LectureRoom, Occupancy, AirQualityLevel) VALUES ('FAB LAB 103', 0, 0.1);
INSERT INTO ROOMINFORMATION (LectureRoom, Occupancy, AirQualityLevel) VALUES ('FAB LAB 203', 0, 0.1);      