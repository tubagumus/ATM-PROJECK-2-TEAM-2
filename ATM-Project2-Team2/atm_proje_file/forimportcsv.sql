PGDMP          9                {            postgres    14.7    14.7                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    13754    postgres    DATABASE     e   CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Turkish_Turkey.1254';
    DROP DATABASE postgres;
                postgres    false                       0    0    DATABASE postgres    COMMENT     N   COMMENT ON DATABASE postgres IS 'default administrative connection database';
                   postgres    false    3334            �            1259    24588    forimportcsv    TABLE     �   CREATE TABLE public.forimportcsv (
    name character varying NOT NULL,
    "3" character varying,
    "5" character varying,
    "6" character varying,
    "7" character varying,
    "2" character varying,
    "4" character varying
);
     DROP TABLE public.forimportcsv;
       public         heap    postgres    false                       0    24588    forimportcsv 
   TABLE DATA           J   COPY public.forimportcsv (name, "3", "5", "6", "7", "2", "4") FROM stdin;
    public          postgres    false    213   �       t           2606    24594    forimportcsv forimportcsv_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.forimportcsv
    ADD CONSTRAINT forimportcsv_pkey PRIMARY KEY (name);
 H   ALTER TABLE ONLY public.forimportcsv DROP CONSTRAINT forimportcsv_pkey;
       public            postgres    false    213                �  x�u��n�0��΃�X��,i�tN�I�C/��Zje)�ew~�)�m�l�R"���Ejk�-^���͞�0�rv����o���V;�?[�8�B���փk�WB����'��Q'Nb�NҶd~0]H�b�[uk>��.����Αkǵ�F�Q�y:���D<C�v�2�<KlM�;"y���4r2�E^?AG�<�h����S.�[,z')� �|2���v�)G���Ǥ��{驦��#���2=ѾQ�5���,���5Ć$}�mH��8L�{UL�.]�䥾�F�#V[J�t
�����
km��{IsgV��ȳ���˾KHƱ�}I_#RGi{��:j0�����Ǐ��$���q!�A�6x&7,�D-!_*�u�:����̈́��<Φh]��a���k�R����M>�W���q��������MިŎp&9M����;����N�����rO��1��*��GT_���q���Q�X�E䎳ȯ�ہ�/b�e��ymC�้1��lB�O �Oho��[7}����Oe��_��r�>3��E8�y,�T�����#ɈZ��ٛ*��=T"���z\(��]���P������m6�]��Une�ׯ��{ӊu7Uh�������f6��n��     