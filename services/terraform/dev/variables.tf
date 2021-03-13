variable "region" {
  description = "This is the cloud hosting region where your webapp will be deployed."
}

variable "prefix" {
  description = "This is the environment where your webapp is deployed. qa, prod, or dev"
}

locals {
  dynamo-user-search-table = "user-search-table-${var.prefix}"
  dynamo-tfids-table = "tfids-table-${var.prefix}"
  dynamo-places-table = "places-table-${var.prefix}"

}