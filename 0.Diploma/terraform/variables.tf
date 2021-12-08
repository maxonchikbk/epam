variable "prefix" {
  default = "MaxChe"
}

variable "location" {
  default = "canadacentral"
}

variable "vm_sku" {
  default = "Standard_DS2_v2"
}

variable "node_count" {
  default = 1
}

variable "ssh_public_key" {
  default = "~/.ssh/id_rsa.pub"
}

variable "scfile" {
  type    = string
  default = "script.sh"
}