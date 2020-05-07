insert into public.educator (educator_id, username, password, name, surname, patronymic) values ('f65f27e8-5430-4ada-8fe7-dd8e9cfa3819', 'Irina', '$2b$12$L4fx5TQC4.9uir2CZve0pOIBp8nj6b3DER2a1dx/RU5Dx1MeQ3sIO', 'Ирина', 'Кузнецова', 'Алексеевна');

INSERT INTO public.child (child_id, educator_id, age, photo_link, blood_type, "group", locker_num, name, surname, patronymic) VALUES ('540a1403-5962-47a0-8197-02afc878786a', 'f65f27e8-5430-4ada-8fe7-dd8e9cfa3819', 3, null, '1', 'одуванчики', 'ромашка', 'Иван', 'Лебедев', 'Александрович');
INSERT INTO public.child (child_id, educator_id, age, photo_link, blood_type, "group", locker_num, name, surname, patronymic) VALUES ('b9ca6b30-814d-4e76-b152-563e893b8155', 'f65f27e8-5430-4ada-8fe7-dd8e9cfa3819', 3, null, '2', 'одуванчики', 'вишня', 'Аня', 'Весёлкина', 'Сергеевна');
INSERT INTO public.child (child_id, educator_id, age, photo_link, blood_type, "group", locker_num, name, surname, patronymic) VALUES ('dcb24ee3-5201-4a5a-bac3-8c211f99e584', 'f65f27e8-5430-4ada-8fe7-dd8e9cfa3819', 3, null, '4', 'одуванчики', 'домик', 'Вася', 'Воропаев', 'Петрович');
INSERT INTO public.child (child_id, educator_id, age, photo_link, blood_type, "group", locker_num, name, surname, patronymic) VALUES ('4c306557-bd2e-4063-8f26-feb7fdeb3a23', 'f65f27e8-5430-4ada-8fe7-dd8e9cfa3819', 3, null, '4', 'одуванчики', 'пчёлка', 'Маша', 'Жданова', 'Дмитриевна');

insert into public.food (food_id, educator_id, name) values ('3305b7dc-3328-4b19-8105-ce42756762a2', 'f65f27e8-5430-4ada-8fe7-dd8e9cfa3819', 'Каша');
insert into public.food (food_id, educator_id, name) values ('489c7046-15eb-451e-a6b3-94750f73ec9e', 'f65f27e8-5430-4ada-8fe7-dd8e9cfa3819', 'Овощной суп');
insert into public.food (food_id, educator_id, name) values ('09d0b572-b13e-4a33-a80d-e547d99193ed', 'f65f27e8-5430-4ada-8fe7-dd8e9cfa3819', 'Пюре');
insert into public.food (food_id, educator_id, name) values ('4dfa2f5d-0b15-449e-bca0-23f72bfa3fc2', 'f65f27e8-5430-4ada-8fe7-dd8e9cfa3819', 'Котлета');
insert into public.food (food_id, educator_id, name) values ('046ed37a-bcbf-4dad-b8f3-d7108581aa73', 'f65f27e8-5430-4ada-8fe7-dd8e9cfa3819', 'Компот');
