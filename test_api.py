import requests
import json

# URL base da sua API Flask
BASE_URL = "http://127.0.0.1:5000/items"

def run_tests():
    # --- 1. GET para ver a lista antes ---
    print("\n--- 1. Lista Inicial ---")
    response = requests.get(BASE_URL)
    initial_items = response.json()
    print(json.dumps(initial_items, indent=2, ensure_ascii=False))

    # --- 2. DELETE o item com ID 2 ---
    ITEM_ID_TO_DELETE = 2
    print(f"\n--- 2. Tentando DELETAR o Item ID {ITEM_ID_TO_DELETE} ---")
    
    # Faz a requisição DELETE
    delete_response = requests.delete(f"{BASE_URL}/{ITEM_ID_TO_DELETE}")
    
    # Verifica o código de status HTTP
    if delete_response.status_code == 204:
        print(f"Sucesso! Item {ITEM_ID_TO_DELETE} deletado (Status 204 No Content).")
    else:
        print(f"Falha ao deletar. Status Code: {delete_response.status_code}")
        
    # --- 3. GET para confirmar a exclusão ---
    print("\n--- 3. Lista Após o DELETE ---")
    response = requests.get(BASE_URL)
    final_items = response.json()
    print(json.dumps(final_items, indent=2, ensure_ascii=False))
    
    # Verifica se o item 2 realmente sumiu da lista final
    found_deleted_item = next((item for item in final_items if item["id"] == ITEM_ID_TO_DELETE), None)
    
    if found_deleted_item is None:
        print(f"\nConfirmação: Item {ITEM_ID_TO_DELETE} NÃO está mais na lista. SUCESSO TOTAL!")
    else:
        print(f"\nERRO: Item {ITEM_ID_TO_DELETE} ainda está na lista.")


if __name__ == "__main__":
    run_tests()