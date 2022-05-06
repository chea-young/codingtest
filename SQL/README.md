## SQL coding test 준비 (MYSQL)

### 조회(SELECT)
- SELECT FROM

### 정렬 ORDER BY
- 오름차 순: `ORDER BY 기준열`
- 내림차 순: `ORDER BY 기준열 DESC`
- 다중 정렬: `ORDER BY 필드1, 필드2`

### 조건절 WHERE
- 하나의 기준열만 비교: `WHERE 기준열=비교하고 싶은 것`
- 해당 조건이 아닌 경우: `WHERE NOT 기준열=비교하고 싶은 것`
- NULL 검색: `WHERE 기준열 IS NOT NULL`
- 문자열 검색: `WHERE 기준열 LIKE "*문자열*"`
    - `%`: 문자열
    - `*` : 하나의 문자일
    - `#` : 하나의 숫자
- 조건절
    - =, <=, >=
    - and, or, NOT

### 최대, 최소 MAX, MIN
- 최대값: `SELECT MAX(컬럼) FROM 테이블;`
- 최소값: `SELECT MIN(컬럼) FROM 테이블;`

### JOIN
- 두 개의 테이블 간의 컬럼 값들이 서로 정확하게 일치하는 경우, 사용되며 대부분 PK-FK 관계를 기반
- 별칭 사용
```
SELECT S.id, G.grade
FROM Student S, Grade G         
WHERE S.id = G.id
AND G.grade > 3.5;
ORDER BY G.grade DESC;
```
- Non-EQUIJOIN 비등가 조인(같은 값을 갖지 않을 때 사용)
    - "=" 연산자가 아닌, Between, >, >= 와 같은 연산자를 이용
    ```
    SELECT 테이블1.컬럼명, 테이블2.컬럼명
    FROM 테이블1, 테이블2
    WHERE 테이블1.컬럼명1 BETWEEN 테이블2.컬럼명1 AND 테이블2.컬럼명2;
    ```
- LEFT JOIN
    -A값의 전체와, A의 KEY 값과 B KEY 값이 같은 결과
    ```
    SELECT ~~
    FROM TABLE_A
    LEFT JOIN TABLE_B ON TABLE_A.KEY = TABLE_B.KEY
    ```

### DISTINCT
- 원하는 컬럼을 나열하면 중복 값이 제거된 데이터를 가져오는 것이 가능
```
SELECT DISTINCT 칼럼1, 칼럼2
SELECT COUNT(DISTINCT 칼럼1)
```

### GROUP BY
- 해당 칼럼으로 묶어서 데이터를 조회하기 위해 사용
- GROUP BY로 조건을 줄 때에는 HAVING 절을 이용

### DATETIME
- 시간을 나타내는 데이터 타입
- HOUR(칼럼1) : 시간만 추출
- YEAR(칼럼1) : 년도만 추출 