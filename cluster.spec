metadata:
  creationTimestamp: 2019-08-27T22:07:09Z
  name: almatronics.es
spec:
  api:
    loadBalancer:
      sslCertificate: arn:aws:acm:eu-west-1:975195398054:certificate/1e526dd6-1b47-4f95-a9b5-2175f01dc66d
      type: Internal
  authorization:
    rbac: {}
  channel: stable
  cloudLabels:
    Owner: Alvaro Almanza
    Team: ciberseguridad-ui1
  cloudProvider: aws
  clusterDNSDomain: cluster.local
  configBase: s3://kops-masterui1/almatronics.es
  configStore: s3://kops-masterui1/almatronics.es
  dnsZone: almatronics.es
  docker:
    ipMasq: false
    ipTables: false
    logDriver: json-file
    logLevel: warn
    logOpt:
    - max-size=10m
    - max-file=5
    storage: overlay2,overlay,aufs
    version: 18.06.3
  etcdClusters:
  - backups:
      backupStore: s3://kops-masterui1/almatronics.es/backups/etcd/main
    cpuRequest: 200m
    enableEtcdTLS: true
    enableTLSAuth: true
    etcdMembers:
    - instanceGroup: master-eu-west-1a
      name: a
    manager: {}
    memoryRequest: 100Mi
    name: main
    provider: Manager
    version: 3.2.24
  - backups:
      backupStore: s3://kops-masterui1/almatronics.es/backups/etcd/events
    cpuRequest: 100m
    enableEtcdTLS: true
    enableTLSAuth: true
    etcdMembers:
    - instanceGroup: master-eu-west-1a
      name: a
    manager: {}
    memoryRequest: 100Mi
    name: events
    provider: Manager
    version: 3.2.24
  iam:
    allowContainerRegistry: true
    legacy: false
  keyStore: s3://kops-masterui1/almatronics.es/pki
  kubeAPIServer:
    allowPrivileged: true
    anonymousAuth: false
    apiServerCount: 1
    authorizationMode: RBAC
    bindAddress: 0.0.0.0
    cloudProvider: aws
    enableAdmissionPlugins:
    - NamespaceLifecycle
    - LimitRanger
    - ServiceAccount
    - PersistentVolumeLabel
    - DefaultStorageClass
    - DefaultTolerationSeconds
    - MutatingAdmissionWebhook
    - ValidatingAdmissionWebhook
    - NodeRestriction
    - ResourceQuota
    etcdServers:
    - http://127.0.0.1:4001
    etcdServersOverrides:
    - /events#http://127.0.0.1:4002
    image: k8s.gcr.io/kube-apiserver:v1.12.10
    insecureBindAddress: 127.0.0.1
    insecurePort: 8080
    kubeletPreferredAddressTypes:
    - InternalIP
    - Hostname
    - ExternalIP
    logLevel: 2
    requestheaderAllowedNames:
    - aggregator
    requestheaderExtraHeaderPrefixes:
    - X-Remote-Extra-
    requestheaderGroupHeaders:
    - X-Remote-Group
    requestheaderUsernameHeaders:
    - X-Remote-User
    securePort: 443
    serviceClusterIPRange: 100.64.0.0/13
    storageBackend: etcd3
  kubeControllerManager:
    allocateNodeCIDRs: true
    attachDetachReconcileSyncPeriod: 1m0s
    cloudProvider: aws
    clusterCIDR: 100.96.0.0/11
    clusterName: almatronics.es
    configureCloudRoutes: false
    image: k8s.gcr.io/kube-controller-manager:v1.12.10
    leaderElection:
      leaderElect: true
    logLevel: 2
    useServiceAccountCredentials: true
  kubeDNS:
    cacheMaxConcurrent: 150
    cacheMaxSize: 1000
    cpuRequest: 100m
    domain: cluster.local
    memoryLimit: 170Mi
    memoryRequest: 70Mi
    replicas: 2
    serverIP: 100.64.0.10
  kubeProxy:
    clusterCIDR: 100.96.0.0/11
    cpuRequest: 100m
    hostnameOverride: '@aws'
    image: k8s.gcr.io/kube-proxy:v1.12.10
    logLevel: 2
  kubeScheduler:
    image: k8s.gcr.io/kube-scheduler:v1.12.10
    leaderElection:
      leaderElect: true
    logLevel: 2
  kubelet:
    allowPrivileged: true
    anonymousAuth: false
    cgroupRoot: /
    cloudProvider: aws
    clusterDNS: 100.64.0.10
    clusterDomain: cluster.local
    enableDebuggingHandlers: true
    evictionHard: memory.available<100Mi,nodefs.available<10%,nodefs.inodesFree<5%,imagefs.available<10%,imagefs.inodesFree<5%
    featureGates:
      ExperimentalCriticalPodAnnotation: "true"
    hostnameOverride: '@aws'
    kubeconfigPath: /var/lib/kubelet/kubeconfig
    logLevel: 2
    networkPluginName: cni
    nonMasqueradeCIDR: 100.64.0.0/10
    podInfraContainerImage: k8s.gcr.io/pause-amd64:3.0
    podManifestPath: /etc/kubernetes/manifests
  kubernetesApiAccess:
  - 10.0.0.0/16
  kubernetesVersion: 1.12.10
  masterInternalName: api.internal.almatronics.es
  masterKubelet:
    allowPrivileged: true
    anonymousAuth: false
    cgroupRoot: /
    cloudProvider: aws
    clusterDNS: 100.64.0.10
    clusterDomain: cluster.local
    enableDebuggingHandlers: true
    evictionHard: memory.available<100Mi,nodefs.available<10%,nodefs.inodesFree<5%,imagefs.available<10%,imagefs.inodesFree<5%
    featureGates:
      ExperimentalCriticalPodAnnotation: "true"
    hostnameOverride: '@aws'
    kubeconfigPath: /var/lib/kubelet/kubeconfig
    logLevel: 2
    networkPluginName: cni
    nonMasqueradeCIDR: 100.64.0.0/10
    podInfraContainerImage: k8s.gcr.io/pause-amd64:3.0
    podManifestPath: /etc/kubernetes/manifests
    registerSchedulable: false
  masterPublicName: api.almatronics.es
  networkCIDR: 10.0.0.0/16
  networkID: vpc-0a5ea6c1bddd46fe2
  networking:
    flannel:
      backend: vxlan
  nonMasqueradeCIDR: 100.64.0.0/10
  secretStore: s3://kops-masterui1/almatronics.es/secrets
  serviceClusterIPRange: 100.64.0.0/13
  sshAccess:
  - 10.0.0.0/16
  subnets:
  - cidr: 10.0.4.0/24
    id: subnet-0bb0b6050fb1adce4
    name: eu-west-1a
    type: Private
    zone: eu-west-1a
  - cidr: 10.0.5.0/24
    id: subnet-08ba1774dcf9b1097
    name: eu-west-1b
    type: Private
    zone: eu-west-1b
  - cidr: 10.0.6.0/24
    id: subnet-0946e6b4e65a56f1a
    name: eu-west-1c
    type: Private
    zone: eu-west-1c
  topology:
    dns:
      type: Public
    masters: private
    nodes: private
