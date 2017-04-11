delete from provider_product_revisions where provider_product_id in (select id from provider_products where full_name like '%QA TESTING%');
delete from insurer_product_revisions where insurer_product_id in (select id from insurer_products where full_name like '%QA TESTING%');
delete from provider_products where full_name like '%QA TESTING%';
delete from insurer_products where full_name like '%QA TESTING%';
delete from pbm.product_categories where id>=10000000;
delete from pbm.substitute_products where id>=10000000;
delete from public.insurer_product_diagnoses where product_diagnosis_id in (select id from public.product_diagnoses where diagnosis_id>=10000000 );
delete from public.product_diagnoses where diagnosis_id in (select id from public.diagnoses where name like '%QA TESTING%');
delete from public.diagnoses where name like '%QA TESTING%';