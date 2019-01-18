control "vagrant" do
  title "vagrant role check"

  describe command('vagrant') do
      it { should exist }
    end

end
