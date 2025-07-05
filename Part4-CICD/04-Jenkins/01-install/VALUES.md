# Jenkins Helm Values Configuration Examples

## Basic values.yaml Examples

### 1. Production Configuration with LoadBalancer
```yaml
controller:
  serviceType: LoadBalancer
  resources:
    requests:
      cpu: "500m"
      memory: "1Gi"
    limits:
      cpu: "2000m"
      memory: "4Gi"
  
persistence:
  enabled: true
  size: "20Gi"
  storageClass: "gp2"

agent:
  resources:
    requests:
      cpu: "200m"
      memory: "256Mi"
    limits:
      cpu: "500m"
      memory: "512Mi"
```

### 2. Development Configuration with NodePort
```yaml
controller:
  serviceType: NodePort
  nodePort: 32000
  resources:
    requests:
      cpu: "200m"
      memory: "512Mi"
    limits:
      cpu: "1000m"
      memory: "2Gi"

persistence:
  enabled: true
  size: "8Gi"
```

### 3. Custom Admin User
```yaml
controller:
  admin:
    username: "admin"
    password: "your-secure-password"
  
  # Install additional plugins
  installPlugins:
    - kubernetes:latest
    - workflow-aggregator:latest
    - git:latest
    - configuration-as-code:latest
    - blueocean:latest
```

### 4. Security Configuration
```yaml
controller:
  # Enable CSRF protection
  csrf:
    defaultCrumbIssuer:
      enabled: true
      proxyCompatability: true
  
  # JCasC configuration
  JCasC:
    enabled: true
    defaultConfig: true
```

## Usage
1. Create a `values.yaml` file with your desired configuration
2. Install Jenkins with custom values:
```bash
helm install jenkins jenkinsci/jenkins -f values.yaml
```

## Get Full Values Reference
```bash
helm show values jenkinsci/jenkins > full-values.yaml
```