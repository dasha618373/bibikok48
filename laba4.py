#Вариант 1
#Задание 2
from Bio import SeqIO

file_path = "E:\example cds.gb" 
records = []


for record in SeqIO.parse(file_path, "genbank"):
    gc_content = (record.seq.count("G") + record.seq.count("C")) / len(record.seq)
    records.append((record.id, record.description, gc_content))

# Сортируем записи по GC-составу
records.sort(key=lambda x: x[2])

# Выводим результат
for record_id, description, gc_content in records:
    print(f"{record_id}: {description}, GC = {gc_content:.5f}")
#Задание 3
from Bio import SeqIO

def translate_cds(record):
    """Функция для трансляции кодирующей последовательности"""
    for feature in record.features:
        if feature.type == "CDS":
            start, end = feature.location.start, feature.location.end
            protein_seq = feature.qualifiers.get("translation", [""])[0]
            print(f"{record.id}: {record.description}")
            print(f"Coding sequence location = [{start}:{end}]")
            print(f"Translation =\n{protein_seq}\n")

def parse_genbank(file_path):
    """Чтение файла GenBank и трансляция CDS"""
    for record in SeqIO.parse(file_path, "genbank"):
        translate_cds(record)


file_path = "E:\example cds.gb"
parse_genbank(file_path)
