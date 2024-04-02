from pybtex.database import parse_file

def remove_doi_field(bib_input_path, bib_output_path):
    # 解析BibTeX文件，指定编码为utf-8
    bib_data = parse_file(bib_input_path, encoding='utf-8')
    # 遍历所有条目并删除doi字段（如果存在）
    for entry in bib_data.entries.values():
        if 'doi' in entry.fields:
            del entry.fields['doi']
    # 将修改后的BibTeX数据写回文件，同时指定编码为utf-8
    with open(bib_output_path, "w", encoding='utf-8') as bibfile:
        bib_data.to_file(bibfile, bib_format='bibtex')


def main():
    bib_input_path = "./notebook/bib.bib"
    bib_output_path = "./notebook/bib.bib"
    remove_doi_field(bib_input_path, bib_output_path)


if __name__ == "__main__":
    main()