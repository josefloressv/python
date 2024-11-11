terraform {
  required_version = "0.14.5"
  required_providers {
    tls = {
      source  = "hashicorp/tls"
      version = "3.0.0"
    }
    local = {
      source  = "hashicorp/local"
      version = "2.0.0"
    }
  }
}

provider "tls" {
  # Configuration options
}
provider "local" {
  # Configuration options
}

# Create a SSH keypair
# https://registry.terraform.io/providers/hashicorp/tls/latest/docs/resources/private_key
resource "tls_private_key" "ssh_key" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

data "template_file" "cloud_config" {
  template = file("${path.module}/cloud-config.yaml.tpl")

  vars = {
    private_key = indent(4, tls_private_key.ssh_key.private_key_pem)
    public_key  = indent(4, tls_private_key.ssh_key.public_key_pem)
  }
}

# Write tf-key-pair to local file
# https://registry.terraform.io/providers/hashicorp/local/latest/docs/resources/file
resource "local_file" "cloud_config" {
  content  = data.template_file.cloud_config.rendered
  filename = "cloud-config.yaml"
}