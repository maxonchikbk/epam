terraform {
  required_providers {
    kubectl = {
      source  = "gavinbunney/kubectl"
      version = ">= 1.7.0"
    }
  }
}

provider "helm" {
  kubernetes {
    config_path = "~/.kube/config"
  }
}

provider "kubectl" {
  load_config_file = true
  config_path      = "~/.kube/config"
}

resource "helm_release" "ingress-nginx" {
  name = "ingress-nginx"

  repository = "https://kubernetes.github.io/ingress-nginx"
  chart      = "ingress-nginx"

  set {
    name  = "service.type"
    value = "ClusterIP"
  }
}

resource "helm_release" "kube-prometheus-stack" {
  name = "kube-prometheus-stack"

  repository = "https://prometheus-community.github.io/helm-charts"
  chart      = "kube-prometheus-stack"

  values = [
    "${file("values.cfg")}"
  ]
}

data "kubectl_filename_list" "namespace" {
  pattern = "../../kubernetes/ns-*.yaml"
}

resource "kubectl_manifest" "namespace" {
  count     = length(data.kubectl_filename_list.namespace.matches)
  yaml_body = file(element(data.kubectl_filename_list.namespace.matches, count.index))
}

data "kubectl_filename_list" "service" {
  pattern = "../../kubernetes/service-*.yaml"
}

resource "kubectl_manifest" "service" {    
  count     = length(data.kubectl_filename_list.service.matches)
  yaml_body = file(element(data.kubectl_filename_list.service.matches, count.index))

  depends_on = [kubectl_manifest.namespace]
}

data "kubectl_filename_list" "ingress" {
  pattern = "../../kubernetes/ingress-*.yaml"
}

resource "kubectl_manifest" "ingress" {
  count     = length(data.kubectl_filename_list.ingress.matches)
  yaml_body = file(element(data.kubectl_filename_list.ingress.matches, count.index))

  depends_on = [kubectl_manifest.namespace]
}