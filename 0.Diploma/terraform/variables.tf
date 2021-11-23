variable "prefix" {
  default     = "MaxChe"  
}

variable "location" {
  default     = "southcentralus"  
}

variable "node_count"{
  default = 3  
}

variable "ssh_public_key" {
    default = "~/.ssh/id_rsa.pub"
}
