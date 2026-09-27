CREATE TABLE Book (
  bookid NUMBER(2) PRIMARY KEY,
  bookname VARCHAR2(40),
  publisher VARCHAR2(40),
  price NUMBER(8)
);

CREATE TABLE Customer (
  custid NUMBER(2) PRIMARY KEY,
  name VARCHAR2(40),
  address VARCHAR2(50),
  phone VARCHAR2(20)
);

CREATE TABLE Orders (
  orderid NUMBER(2) PRIMARY KEY,
  custid NUMBER(2) REFERENCES Customer(custid),
  bookid NUMBER(2) REFERENCES Book(bookid),
  saleprice NUMBER(8),
  orderdate DATE
);

/* Book, Customer, Orders 데이터 생성 */
INSERT INTO Book VALUES(1, '축구의 역사', '굿스포츠', 7000);
INSERT INTO Book VALUES(2, '축구아는 여자', '나무수', 13000);
INSERT INTO Book VALUES(3, '축구의 이해', '대한미디어', 22000);
INSERT INTO Book VALUES(4, '골프 바이블', '대한미디어', 35000);
INSERT INTO Book VALUES(5, '피겨 교본', '굿스포츠', 8000);
INSERT INTO Book VALUES(6, '역도 단계별기술', '굿스포츠', 6000);
INSERT INTO Book VALUES(7, '야구의 추억', '이상미디어', 20000);
INSERT INTO Book VALUES(8, '야구를 부탁해', '이상미디어', 13000);
INSERT INTO Book VALUES(9, '올림픽 이야기', '삼성당', 7500);
INSERT INTO Book VALUES(10, 'Olympic Champions', 'Pearson', 13000);

INSERT INTO Customer VALUES (1, '박지성', '영국 맨체스타', '000-5000-0001');
INSERT INTO Customer VALUES (2, '김연아', '대한민국 서울', '000-6000-0001');
INSERT INTO Customer VALUES (3, '장미란', '대한민국 강원도', '000-7000-0001');
INSERT INTO Customer VALUES (4, '추신수', '미국 클리블랜드', '000-8000-0001');
INSERT INTO Customer VALUES (5, '박세리', '대한민국 대전', NULL);

INSERT INTO Orders VALUES (1, 1, 1, 6000, TO_DATE('2020-07-01','yyyy-mm-dd'));
INSERT INTO Orders VALUES (2, 1, 3, 21000, TO_DATE('2020-07-03','yyyy-mm-dd'));
INSERT INTO Orders VALUES (3, 2, 5, 8000, TO_DATE('2020-07-03','yyyy-mm-dd'));
INSERT INTO Orders VALUES (4, 3, 6, 6000, TO_DATE('2020-07-04','yyyy-mm-dd'));
INSERT INTO Orders VALUES (5, 4, 7, 20000, TO_DATE('2020-07-05','yyyy-mm-dd'));
INSERT INTO Orders VALUES (6, 1, 2, 12000, TO_DATE('2020-07-07','yyyy-mm-dd'));
INSERT INTO Orders VALUES (7, 4, 8, 13000, TO_DATE('2020-07-07','yyyy-mm-dd'));
INSERT INTO Orders VALUES (8, 3, 10, 12000, TO_DATE('2020-07-08','yyyy-mm-dd'));
INSERT INTO Orders VALUES (9, 2, 10, 7000, TO_DATE('2020-07-09','yyyy-mm-dd'));
INSERT INTO Orders VALUES (10, 3, 8, 13000, TO_DATE('2020-07-10','yyyy-mm-dd'));

CREATE TABLE Imported_Book (
  bookid NUMBER,
  bookname VARCHAR2(40),
  publisher VARCHAR2(40),
  price NUMBER(8)
);

SELECT phone
FROM Customer
WHERE name='김연아';

SELECT bookname, price
FROM book;

SELECT price, bookname
FROM book;

SELECT bookid, bookname, publisher, price
FROM book;

SELECT *
FROM book;

SELECT DISTINCT publisher -- DISTINCT - 중복 제거
FROM book;

SELECT *
FROM book
WHERE price < 20000;

SELECT *
FROM book
WHERE price BETWEEN 10000 AND 20000;

SELECT *
FROM book
WHERE price >= 10000 AND price <= 20000;

SELECT *
FROM book
WHERE publisher IN('굿스포츠', '대한미디어');

SELECT *
FROM book
WHERE publisher NOT IN('굿스포츠', '대한미디어');

SELECT bookname, publisher
FROM book
WHERE bookname LIKE '축구의 역사';

SELECT bookname, publisher
FROM book
WHERE bookname LIKE '%축구%';

SELECT *
FROM book
WHERE bookname LIKE '_구%';

SELECT *
FROM book
WHERE bookname LIKE '%축구%' AND price >= 20000;

SELECT *
FROM book
ORDER BY bookname;

SELECT *
FROM book
ORDER BY price DESC, publisher ASC; -- SQL에서는 , 가 같다면의 뜻 ','를 계속 붙이면 계속 가능

SELECT SUM(saleprice) AS totalprice -- as로 속성의 이름 변경 가능
FROM Orders;

SELECT SUM(saleprice) AS 김연아매출
FROM Orders
WHERE custid = 2;

SELECT SUM(saleprice) AS Total,
       AVG(saleprice) AS Averager,
       MIN(saleprice) AS Minimum,
       MAX(saleprice) AS Maximum
From Orders;

SELECT COUNT(*)
FROM Orders;

SELECT custid, COUNT(*) AS 도서수량, SUM(saleprice) AS 총액
FROM Orders
GROUP BY custid;

SELECT custid, COUNT(*) AS 도서수량
FROM Orders
WHERE saleprice >= 8000
GROUP BY custid
HAVING count(*) >= 2;

SELECT *
FROM Customer, Orders;

SELECT *
FROM Customer, Orders
WHERE Customer.custid=Orders.custid;

SELECT *
FROM Customer, Orders
WHERE Customer.custid = Orders.custid
ORDER BY Customer.custid;

SELECT name, saleprice
FROM Customer, Orders
WHERE Customer.custid = Orders.custid;
-- ORDER BY customer.name; 이름 순 정렬이 필요할 때

SELECT name, SUM(saleprice) AS 총액
FROM Customer, Orders
WHERE Customer.custid = Orders.custid
GROUP BY Customer.name
ORDER BY Customer.name;

SELECT name, book.bookname
FROM Customer, Orders, Book
WHERE Customer.custid = Orders.custid AND Orders.bookid = Book.bookid;

SELECT name, book.bookname
FROM Customer, Orders, Book
WHERE Customer.custid = Orders.custid AND Orders.bookid = Book.bookid AND Orders.saleprice = 20000; -- 실제 판매한 금액임, 할인 등이 모두 적용됨
-- 그렇지 않으려면 Book.price 가 맞음 (정가)

SELECT Customer.name, saleprice
FROM Customer LEFT OUTER JOIN Orders ON Customer.custid = Orders.custid;

SELECT Customer.name, COUNT(*) AS 주문갯수, SUM(saleprice) AS 총액
FROM Customer LEFT OUTER JOIN Orders ON Customer.custid = Orders.custid
GROUP BY Customer.name
ORDER BY Customer.name;

SELECT Customer.name, SUM(Orders.saleprice)-- Quiz 01
FROM Customer, Orders
WHERE Customer.custid = Orders.custid
GROUP BY Customer.name
ORDER BY Customer.name;

SELECT Customer.name, SUM(Orders.saleprice) -- QUIZ 02
FROM Customer, Orders
WHERE Customer.custid = Orders.custid
GROUP BY Customer.name
HAVING SUM(Orders.saleprice) >= 20000
ORDER BY Customer.name;

SELECT Orders.custid, COUNT(*) -- QUIZ 03
FROM Orders
WHERE Orders.saleprice >= 8000
GROUP BY Orders.custid
HAVING count(*) >= 2;

-------------------------------------------------- subquery -------------------
SELECT bookname, price
FROM Book
WHERE price > (SELECT AVG(Book.price) FROM BOOK);

SELECT name
FROM Customer
WHERE custid IN (SELECT Orders.custid FROM Orders);

