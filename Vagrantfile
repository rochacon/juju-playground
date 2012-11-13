# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant::Config.run do |config|
  config.vm.box = "juju"
  config.vm.customize ["modifyvm", :id, "--memory", 4096]
  config.vm.network :bridged
end
