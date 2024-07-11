-- 코드를 입력하세요
SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') 
from MEMBER_PROFILE
Where (TLNO != '' or TLNO = null) and (Gender = 'W' And Month(DATE_OF_BIRTH) = 3);