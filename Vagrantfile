# -*- mode: ruby -*-
# vi: set ft=ruby :
 
Vagrant.configure("2") do |config|
  config.vm.box = "opscode_centos-6.3_chef-11.2.0"
  config.vm.box_url = "https://opscode-vm.s3.amazonaws.com/vagrant/opscode_centos-6.3_chef-11.2.0.box"
 
  config.vm.hostname = "vagrant-dd"
 
  config.vm.provision :chef_solo do |chef|
    chef.log_level = :debug

    chef.add_recipe "datadog::apache"
    chef.add_recipe "datadog::cassandra"
    chef.add_recipe "datadog::couchdb"
    chef.add_recipe "datadog::elasticsearch"
    chef.add_recipe "datadog::haproxy"
    chef.add_recipe "datadog::nginx"
    chef.add_recipe "datadog::memcache"
    chef.add_recipe "datadog::jenkins"
    chef.add_recipe "datadog::kyototycoon"
    chef.add_recipe "datadog::lighttpd"
    chef.add_recipe "datadog::mongo"
 
    chef.json = {
      :datadog => {
        :api_key => "nah",
        :haproxy => {
          :instances => [
                         {
                           :url => "http://localhost/admin?stats",
                           :username => "me!",
                           :password => "yeahright"
                         }
                        ]
        },
        :couch => {
          :instances => [
                         {
                           :server => "localhost"
                         }
                        ]
        },
        :cassandra => {
          :instances => [
                         {
                           :server => "localhost",
                           :port => 7199,
                           :instance => "test"
                         }
                        ]
        },
        :apache => {
          :instances => [
                         {
                           :status_url => "http://localost:81/status",
                           :name => "test"
                         }
                        ]
        },
        :nginx => {
          :instances => [
                         {
                           :url => "http://localhost:1234"
                         }
                        ]
        },
        :elasticsearch => {
          :instances => [
                         {
                           :url => "http://localhost:9200"
                         }
                        ]
        },
        :memcache => {
          :instances => [
                         {
                           :server => "localhost"
                         }
                        ]
        },
        :jenkins => {
          :instances => [
                         {
                           :server => "localhost"
                         }
                        ]
        },
        :kyototycoon => {
          :instances => [
                         {
                           :server => "localhost"
                         }
                        ]
        },
        :lighttpd => {
          :instances => [
                         {
                           :server => "localhost"
                         }
                        ]
        },
        :mongo => {
          :instances => [
                         {
                           :server => "localhost"
                         }
                        ]
        },
        :redis => {
          :instances => [
                         {
                           :server => "localhost"
                         }
                        ]
        }
      }
    }
  end
end
