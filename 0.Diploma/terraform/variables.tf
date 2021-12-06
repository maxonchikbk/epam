variable "prefix" {
  default = "MaxChe"
}

variable "location" {
  default = "southcentralus"
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