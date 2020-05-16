INSERT INTO public.educator (educator_id, username, password, name, surname, patronymic) VALUES ('f65f27e8-5430-4ada-8fe7-dd8e9cfa3819', 'Irina', '$2b$12$L4fx5TQC4.9uir2CZve0pOIBp8nj6b3DER2a1dx/RU5Dx1MeQ3sIO', 'Ирина', 'Кузнецова', 'Алексеевна');

INSERT INTO public.child (child_id, educator_id, age, photo_link, blood_type, "group", locker_num, name, surname, patronymic) VALUES ('4c306557-bd2e-4063-8f26-feb7fdeb3a23', 'f65f27e8-5430-4ada-8fe7-dd8e9cfa3819', 3, 'http://82.148.31.234:8000/photos/4c306557-bd2e-4063-8f26-feb7fdeb3a23.jpg', '4', 'одуванчики', 'пчёлка', 'Маша', 'Жданова', 'Дмитриевна');
INSERT INTO public.child (child_id, educator_id, age, photo_link, blood_type, "group", locker_num, name, surname, patronymic) VALUES ('540a1403-5962-47a0-8197-02afc878786a', 'f65f27e8-5430-4ada-8fe7-dd8e9cfa3819', 3, 'http://82.148.31.234:8000/photos/placeholder.jpg', '1', 'одуванчики', 'ромашка', 'Иван', 'Лебедев', 'Александрович');
INSERT INTO public.child (child_id, educator_id, age, photo_link, blood_type, "group", locker_num, name, surname, patronymic) VALUES ('dcb24ee3-5201-4a5a-bac3-8c211f99e584', 'f65f27e8-5430-4ada-8fe7-dd8e9cfa3819', 3, 'http://82.148.31.234:8000/photos/placeholder.jpg', '4', 'одуванчики', 'домик', 'Вася', 'Воропаев', 'Петрович');
INSERT INTO public.child (child_id, educator_id, age, photo_link, blood_type, "group", locker_num, name, surname, patronymic) VALUES ('b9ca6b30-814d-4e76-b152-563e893b8155', 'f65f27e8-5430-4ada-8fe7-dd8e9cfa3819', 3, 'http://82.148.31.234:8000/photos/placeholder.jpg', '2', 'одуванчики', 'вишня', 'Аня', 'Весёлкина', 'Сергеевна');

INSERT INTO public.parent (parent_id, child_id, username, password, relation_degree, phone, photo_link, name, surname, patronymic) VALUES ('0a66d6a3-82c6-49a3-b68d-879ecf7b642c', null, 'ShvalevPetr', '$2b$12$WLmnoyKk1aV4BWuvfKBp9uN4jfbTIeHMJS/5DslfEVFlpPsFQhp66', 'Отец', '89357392947', 'http://82.148.31.234:8000/photos/placeholder.jpg', 'Петр', 'Швалёв', 'Романович');
INSERT INTO public.parent (parent_id, child_id, username, password, relation_degree, phone, photo_link, name, surname, patronymic) VALUES ('04927fc8-e266-4dd0-85bb-2da377165d42', '540a1403-5962-47a0-8197-02afc878786a', 'Olga', '$2b$12$VrytNH.H28fVxAUkLKol4.tCTHLniK7KDRIB8B.aKoPQhdEKAqqeK', 'Мама', '89162763892', 'http://82.148.31.234:8000/photos/placeholder.jpg', 'Ольга', 'Лебедева', 'Николаевна');
INSERT INTO public.parent (parent_id, child_id, username, password, relation_degree, phone, photo_link, name, surname, patronymic) VALUES ('326f5e0f-6cd6-4e21-a25a-2d37a9971e0d', '4c306557-bd2e-4063-8f26-feb7fdeb3a23', 'Bob', '$2b$12$WDbl7izlxmXyQiwDYUXEleMaXFz3v65IEeBv11AL39HnKQ65/HJZ.', 'Отец', '89251438975', 'http://82.148.31.234:8000/photos/326f5e0f-6cd6-4e21-a25a-2d37a9971e0d.jpg', 'Петр', 'Воропаев', 'Николаевич');

INSERT INTO public.event (event_id, child_id, date, has_come, has_gone, asleep, awoke, comment) VALUES ('7a5f9051-0222-4005-a494-b3a335060650', '4c306557-bd2e-4063-8f26-feb7fdeb3a23', '2020-05-10', '10:41', '19:25', '13:30', '14:30', '');

INSERT INTO public.food (food_id, educator_id, name) VALUES ('3305b7dc-3328-4b19-8105-ce42756762a2', 'f65f27e8-5430-4ada-8fe7-dd8e9cfa3819', 'Каша');
INSERT INTO public.food (food_id, educator_id, name) VALUES ('489c7046-15eb-451e-a6b3-94750f73ec9e', 'f65f27e8-5430-4ada-8fe7-dd8e9cfa3819', 'Овощной суп');
INSERT INTO public.food (food_id, educator_id, name) VALUES ('09d0b572-b13e-4a33-a80d-e547d99193ed', 'f65f27e8-5430-4ada-8fe7-dd8e9cfa3819', 'Пюре');
INSERT INTO public.food (food_id, educator_id, name) VALUES ('4dfa2f5d-0b15-449e-bca0-23f72bfa3fc2', 'f65f27e8-5430-4ada-8fe7-dd8e9cfa3819', 'Котлета');
INSERT INTO public.food (food_id, educator_id, name) VALUES ('046ed37a-bcbf-4dad-b8f3-d7108581aa73', 'f65f27e8-5430-4ada-8fe7-dd8e9cfa3819', 'Компот');

INSERT INTO public.meal (meal_id, event_id, type) VALUES ('5a85118b-3b63-448b-8397-e47dd8d96c7c', '7a5f9051-0222-4005-a494-b3a335060650', 1);
INSERT INTO public.meal (meal_id, event_id, type) VALUES ('cc47848c-c06b-4e2c-af88-c0d0906bc520', '7a5f9051-0222-4005-a494-b3a335060650', 2);
INSERT INTO public.meal (meal_id, event_id, type) VALUES ('55f79c86-c3be-47e5-9264-34efb0be5f00', '7a5f9051-0222-4005-a494-b3a335060650', 3);

INSERT INTO public.ration (ration_id, meal_id, food_id, denial) VALUES ('6e7085c1-fc14-4b86-9dc9-41a53728e674', '5a85118b-3b63-448b-8397-e47dd8d96c7c', '09d0b572-b13e-4a33-a80d-e547d99193ed', false);
INSERT INTO public.ration (ration_id, meal_id, food_id, denial) VALUES ('7b782f66-e0eb-462e-b292-706cb0006b9a', '5a85118b-3b63-448b-8397-e47dd8d96c7c', '046ed37a-bcbf-4dad-b8f3-d7108581aa73', true);
INSERT INTO public.ration (ration_id, meal_id, food_id, denial) VALUES ('a9e027e0-88c4-439f-bdb2-180d0cd0b7d8', 'cc47848c-c06b-4e2c-af88-c0d0906bc520', '489c7046-15eb-451e-a6b3-94750f73ec9e', false);
INSERT INTO public.ration (ration_id, meal_id, food_id, denial) VALUES ('44682348-b3e3-4b18-b371-1ff5504c4b99', 'cc47848c-c06b-4e2c-af88-c0d0906bc520', '4dfa2f5d-0b15-449e-bca0-23f72bfa3fc2', true);
INSERT INTO public.ration (ration_id, meal_id, food_id, denial) VALUES ('8022a08e-d101-4f81-a4bf-ec60fc1db9f2', 'cc47848c-c06b-4e2c-af88-c0d0906bc520', '046ed37a-bcbf-4dad-b8f3-d7108581aa73', false);
INSERT INTO public.ration (ration_id, meal_id, food_id, denial) VALUES ('eb2a5fc4-4b4b-4811-acf0-f3859dcc2545', '55f79c86-c3be-47e5-9264-34efb0be5f00', '3305b7dc-3328-4b19-8105-ce42756762a2', false);
INSERT INTO public.ration (ration_id, meal_id, food_id, denial) VALUES ('a63a132a-9767-42c7-a7f7-424fa5c03f5b', '55f79c86-c3be-47e5-9264-34efb0be5f00', '046ed37a-bcbf-4dad-b8f3-d7108581aa73', false);