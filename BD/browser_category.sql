-- Table: public.browser_category

-- DROP TABLE public.browser_category;

CREATE TABLE public.browser_category
(
  "idCategory" integer NOT NULL DEFAULT nextval('"browser_category_idCategory_seq"'::regclass),
  name character varying(60) NOT NULL,
  description text NOT NULL,
  CONSTRAINT browser_category_pkey PRIMARY KEY ("idCategory")
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.browser_category
  OWNER TO trixdiscover;
