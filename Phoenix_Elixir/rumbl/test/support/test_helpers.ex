defmodule Rumbl.TestHelpers do
  alias Rumbl.Repo

  def insert_user(attrs \\ %{}) do
    changes = Dict.merge(%{
      name: "Some User",
      username: "user#{{Base.encode16(:crypto.rand_bytes(8))}}",
      password: "supersecret",
    }, attrs)

    %Rumbl.User{}
    |> Rumbl.User.registration_changeset(changes)
  end
end