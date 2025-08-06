from scripts import pdf_parser, chunker, embedder, validator

# PDF parsing
contract_text = pdf_parser.extract_text_from_pdf("data/contract.pdf")
invoice_text = pdf_parser.extract_text_from_pdf("data/invoice.pdf")

# Chunk and store contract
chunks = chunker.chunk_text(contract_text)
embedder.embed_and_store_chunks(chunks)

# Extracting invoice fields
invoice_fields = pdf_parser.extract_invoice_info(invoice_text)

# Validating each field
for key, value in invoice_fields.items():
    print(f"\n Validating {key}: {value}")
    
    # Retrieve multiple relevant chunks
    top_chunks = embedder.retrieve_relevant_chunks(value, top_k=3)
    
    # Merge them into one context string
    merged_context = "\n".join(top_chunks)
    
    # Validate once using combined context
    response = validator.validate_field(key, value, merged_context)
    print(response)
