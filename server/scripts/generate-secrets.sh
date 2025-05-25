kubectl create secret generic backend-secrets \
  --from-env-file=.env \
  --namespace=backend \
  --dry-run=client \
  --outputs=yaml > backend.secrets.yaml

mv backend.secrets.yaml ../k8s/server 