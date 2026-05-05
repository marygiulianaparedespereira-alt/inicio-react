SELECT *FROM inhabitant
SELECT * FROM inhabitant WHERE job= 'butcher'
SELECT * FROM inhabitant WHERE state = 'friendly'
SELECT * FROM inhabitant WHERE state=  'friendly' AND job = 'weaponsmith'
SELECT * FROM inhabitant WHERE state = 'friendly' AND job LIKE '%smith'
SELECT  personid from inhabitant where name='Stranger'
SELECT  gold from inhabitant where name='Stranger'
SELECT * from item WHERE owner IS NULL
UPDATE item SET owner =20 WHERE owner IS NULL
SELECT * from item WHERE owner=20
select *from inhabitant where job = 'merchant' or job='dealer'  and state ='friendly'
UPDATE item set owner=15 where item 'ring' or item
select *from inhabitant where job LIKE 'biker'