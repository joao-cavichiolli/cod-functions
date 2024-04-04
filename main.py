import os
import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Use o DefaultAzureCredential para autenticar a aplicação com o Azure
    credential = DefaultAzureCredential()

    # Substitua 'YOUR_KEY_VAULT_URL' pelo URL do seu Azure Key Vault
    key_vault_url = "https://aks-kv-teste.vault.azure.net/"

    # Crie um cliente de segredo com o URL do Key Vault e as credenciais
    client = SecretClient(vault_url=key_vault_url, credential=credential)

    # Recupere o segredo do Key Vault
    secret_name = "bduser"
    secret_value = client.get_secret(secret_name).value

    # Use o valor do segredo
    if secret_value:
        return func.HttpResponse(f"Valor do segredo: {secret_value}")
    else:
        return func.HttpResponse("Segredo não encontrado.", status_code=404)
