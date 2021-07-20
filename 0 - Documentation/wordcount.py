import docx2txt

# Loading word document
doc="Chandler_Linguistik_B_A_Theisis_SoSe2021.docx"
my_text = docx2txt.process(doc)

#Characters to not be counted
non_count=6229
limit=75000

doc_count=len([char for char in my_text])

charcount=round(doc_count-non_count-(doc_count*0.0015))
res=round(charcount/limit*100,2)
print(f"{charcount} written out of {limit}.")
print(f"{res} has been completed")
