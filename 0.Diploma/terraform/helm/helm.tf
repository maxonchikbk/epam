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
    config_path = "~/.kube/config"
}

resource "helm_release" "ingress-nginx" {
  name       = "ingress-nginx"

  repository = "https://kubernetes.github.io/ingress-nginx"
  chart      = "ingress-nginx"

  set {
    name  = "service.type"
    value = "ClusterIP"
  }
}

resource "helm_release" "kube-prometheus-stack" {
  name       = "kube-prometheus-stack"

  repository = "https://prometheus-community.github.io/helm-charts"
  chart      = "kube-prometheus-stack"

  values = [
    "${file("values.cfg")}"
  ]
}

data "kubectl_filename_list" "ingress" {
    pattern = "../../kubernetes/*.yaml"
}

resource "kubectl_manifest" "ingress" {
    count = length(data.kubectl_filename_list.ingress.matches)
    yaml_body = file(element(data.kubectl_filename_list.ingress.matches, count.index))
}

data "kubectl_filename_list" "postgres" {
    pattern = "../../kubernetes/postgres/*.yaml"
}

resource "kubectl_manifest" "postgres" {
    count = length(data.kubectl_filename_list.postgres.matches)
    yaml_body = file(element(data.kubectl_filename_list.postgres.matches, count.index))
}

data "kubectl_filename_list" "flask" {
    pattern = "../../kubernetes/flask/*.yaml"
}

resource "kubectl_manifest" "flask" {
    count = length(data.kubectl_filename_list.flask.matches)
    yaml_body = file(element(data.kubectl_filename_list.flask.matches, count.index))
}

data "kubectl_filename_list" "react" {
    pattern = "../../kubernetes/react/*.yaml"
}

resource "kubectl_manifest" "react" {
    count = length(data.kubectl_filename_list.react.matches)
    yaml_body = file(element(data.kubectl_filename_list.react.matches, count.index))
}
