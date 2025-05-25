kubectl create secret generic frontend-secrets \
  --from-env-file=.env \
  --namespace=frontend \
  --dry-run=client \
  --output=yaml > frontend.secrets.yaml

mv frontend.secrets.yaml ../k8s/client 