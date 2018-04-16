defmodule Rumbl.Repo.Migrations.AdjustingVideos do
  use Ecto.Migration

  def change do
    alter table(:videos) do
      remove :" url"
      add :url, :string
    end
  end
end
